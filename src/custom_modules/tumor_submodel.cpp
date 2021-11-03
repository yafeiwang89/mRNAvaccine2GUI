#include "./tumor_submodel.h"

using namespace PhysiCell;

std::string tumor_submodel_version = "0.1.0";

Submodel_Information tumor_submodel_info;

// this vector has been defined in immune_submodels.h 
// disclare the global variable
extern std::vector<Cell*> cells_to_move_from_edge; 

void tumor_submodel_setup( void )
{
	Cell_Definition* pCD;

	// set up any submodels you need

	tumor_submodel_info.name = "tumor model";
	tumor_submodel_info.version = tumor_submodel_version;
	// set functions
	tumor_submodel_info.main_function = antigen_antibody_main_model;
	tumor_submodel_info.phenotype_function = tumor_phenotype;
	tumor_submodel_info.mechanics_function = tumor_mechanics;

	// what microenvironment variables do you expect?
	// tumor_submodel_info.microenvironment_variables.push_back( "TNF" );

	// what custom data do I need?
	//tumor_submodel_info.cell_variables.push_back( "something" );
	// register the submodel
	tumor_submodel_info.register_model();
	// set functions for the corresponding cell definition
	pCD = find_cell_definition( "tumor cell" );
	pCD->functions.update_phenotype = tumor_submodel_info.phenotype_function;
	pCD->functions.custom_cell_rule = tumor_submodel_info.mechanics_function;
	pCD->functions.contact_function = tumor_contact_function;

	// default value in: https://github.com/MathCancer/PhysiCell/blob/master/core/PhysiCell_cell.cpp
	pCD->parameters.o2_proliferation_saturation = 38.0; 
	pCD->parameters.o2_proliferation_threshold = 5.0; 
	pCD->parameters.o2_reference = 38.0; 

	pCD->parameters.o2_necrosis_threshold = 5; // 5
	pCD->parameters.o2_necrosis_max = 2.5;  // 2.5
	pCD->parameters.max_necrosis_rate = 0.0027777777777778; 

	// necrosis rate for tumor cells
	static int necrosis_index = pCD->phenotype.death.find_death_model_index( PhysiCell_constants::necrosis_death_model ); 
	// pCD->phenotype.death.models[necrosis_index]->transition_rate(0,1) = 9e9;
	// pCD->phenotype.death.models[necrosis_index]->transition_rate(1,2) = 1.15741e5;
	// pCD->phenotype.volume.relative_rupture_volume = 1.0001; 
	

	return;
}


void tumor_contact_function( Cell* pC1, Phenotype& p1, Cell* pC2, Phenotype& p2, double dt )
{
	// elastic adhesions
	standard_elastic_contact_function( pC1,p1, pC2, p2, dt );

	return;
}

void tumor_phenotype( Cell* pCell, Phenotype& phenotype, double dt )
{

	static int start_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );
	static int end_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );
	static int apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );  
	static int necrosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::necrosis_death_model ); 

	static int debris_index = microenvironment.find_density_index( "debris");
	static int ISF_index = microenvironment.find_density_index( "ISF" );

	phenotype.secretion.secretion_rates[ISF_index] = parameters.doubles( "ISF_secretion_rate" ); // 0.1
	phenotype.motility.is_motile = false;

	// oxygen based proliferation and death model
	update_cell_and_death_parameters_O2_based(pCell,phenotype,dt);	
	// std::cout << pCell->parameters.max_necrosis_rate << std::endl;

	// https://github.com/MathCancer/PhysiCell/blob/d45d290dd6e956bcc4c6899ff193748aad54bab4/core/PhysiCell_standard_models.cpp#L776

	// set the necrosis rate as zero in mRNA vaccine project !!!!
	phenotype.death.rates[necrosis_index] = 0.0; 
	
	// T-cell based death
	TCell_induced_apoptosis(pCell, phenotype, dt );

	// if I am dead, remove all adhesions
	if( phenotype.death.dead == true )
	{
		// detach all attached cells
		// remove_all_adhesions( pCell );
		phenotype.secretion.secretion_rates[debris_index] = pCell->custom_data["debris_secretion_rate"];
		phenotype.secretion.secretion_rates[ISF_index] = 0.0; 

		pCell->functions.update_phenotype = NULL;
	}


	return;
}

void tumor_mechanics( Cell* pCell, Phenotype& phenotype, double dt )
{
	// if I'm dead, don't bother
	if( phenotype.death.dead == true )
	{
		// the cell death functions don't automatically turn off custom functions,
		// since those are part of mechanics.
		// remove_all_adhesions( pCell );

		// Let's just fully disable now.
		pCell->functions.custom_cell_rule = NULL;
		pCell->functions.contact_function = NULL;	
		return;
	}

	// bounds check 
	if( check_for_out_of_bounds( pCell , 10.0 ) )
	{ 
		#pragma omp critical 
		{ cells_to_move_from_edge.push_back( pCell ); }
		// replace_out_of_bounds_cell( pCell, 10.0 );
		// return; 
	}	

	return;
}


// CD8+ T cell and antibody-antigen complex effect 

void TCell_induced_apoptosis( Cell* pCell, Phenotype& phenotype, double dt )
{
	static int apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );
	static int debris_index = microenvironment.find_density_index( "debris" );
	static int nR_EB = pCell->custom_data.find_variable_index( "antibody_antigen_complex" ); 	

	static bool CD8_T_enabled = parameters.bools( "cytotoxic_T_response" );  // false;
	static bool antibody_enabled = parameters.bools( "antibody_response" );  // false;

	// static double Ig_antigen_50 = 0.3*parameters.doubles("original_antigen_protein");  // 30% of maximum
	static double Ig_antigen_50 = parameters.doubles("Ig_antigen_50"); // 120
	
	// be careful of original setup in .xml !!!!!
	static double apoptosis_rate = parameters.doubles("default_apoptosis_rate"); // 5.32e-5; 
	static double Ig_induce_apoptosis = parameters.doubles("Ig_induce_apoptosis");  // 0.01, may need to update !!!

	// Hill function
	double Ig_complex = pCell->custom_data[ nR_EB ];  
	double E_Ig = Ig_complex /( Ig_complex + Ig_antigen_50); 
	
	pCell->custom_data["E_Ig_complex"] = E_Ig; // record the complex effect on tumor cell

	if ( antibody_enabled )
	{	
		// Hill function: (1- E)*r_0 + E*r_max
		phenotype.death.rates[apoptosis_index] = (1- E_Ig)*apoptosis_rate + E_Ig* Ig_induce_apoptosis;
	}


	if( pCell->custom_data["TCell_contact_time"] > pCell->custom_data["TCell_contact_death_threshold"] && CD8_T_enabled )
	{
		// make sure to get rid of all adhesions!
		// detach all attached cells
		// remove_all_adhesions( pCell );

		#pragma omp critical
		{
			std::cout << "\t\t\t\t" << pCell << " (of type " << pCell->type_name <<  ") died from T cell contact" << std::endl;
		}

		// induce death
		pCell->start_death( apoptosis_index );
		pCell->phenotype.secretion.secretion_rates[debris_index] = pCell->custom_data["debris_secretion_rate"];

		pCell->functions.update_phenotype = NULL;
	}

	return;
}


// don't put into individual cell models -- needs to be a fast process 
void antigen_antibody_dynamics( Cell* pCell, Phenotype& phenotype, double dt )
{
	static int tumor_cell_type = get_cell_definition("tumor cell").type; 

	static int nAb = microenvironment.find_density_index( "Ig" ); 

	static int nR_EU = pCell->custom_data.find_variable_index( "antigen_protein" ); 
	static int nR_EB = pCell->custom_data.find_variable_index( "antibody_antigen_complex" ); 	
	static int nR_bind = pCell->custom_data.find_variable_index( "antibody_binding_rate" ); 

	// do nothing if dead 
	if( phenotype.death.dead == true )
	{ return; } 

	// if not tumor cell, do nothing         
	if( pCell->type != tumor_cell_type )
	{ return; } 

   	// dt*r_bind *rho* V_cell *R_EU,  rho is possible negative
    double dt_bind = dt* pCell->custom_data[nR_bind]* pCell->nearest_density_vector()[nAb]*
     					phenotype.volume.total* pCell->custom_data[nR_EU];

	if( dt_bind>0 && dt_bind<1 )
	{
		double tmp1 = pCell->nearest_density_vector()[nAb]* phenotype.volume.total;	

		if( tmp1 >=1 )  // make sure at least 1 Ig around cell, otherwise rho is possible negative
		{
			if( UniformRandom()<= dt_bind )
			{
				// don't attach more Ig than the available unbound antigen
				if(pCell->custom_data[nR_EU] >= 1)
				{
					pCell->custom_data[nR_EU] -= 1;
					pCell->custom_data[nR_EB] += 1;

					#pragma omp critical
					{
						pCell->nearest_density_vector()[nAb] -= 1.0 / microenvironment.mesh.dV; 
					}    
				}			
			}
		}
	}


	if( dt_bind >=1 )
	{
		double n_Ig = pCell->nearest_density_vector()[nAb]* phenotype.volume.total;	
        double alpha = dt_bind;
        
        // make sure Ig around cell >= dt_bind
        if(alpha > n_Ig)
        {
        	alpha = n_Ig;
        }
	    double alpha1 = floor( alpha );
	    double alpha2 = alpha - alpha1;

        // don't attach more Ig than the available unbound antigen
        if(alpha1 > pCell->custom_data[nR_EU])
        {
        	alpha1 = pCell->custom_data[nR_EU];
        }
        pCell->custom_data[nR_EU] -= alpha1;
		pCell->custom_data[nR_EB] += alpha1;
		#pragma omp critical
		{
			pCell->nearest_density_vector()[nAb] -= alpha1 / microenvironment.mesh.dV;
		}

		double tmp2 = pCell->nearest_density_vector()[nAb]* phenotype.volume.total;	

		if( tmp2 >=1 )  // make sure at least 1 Ig around cell, otherwise rho is possible negative
		{
			if( UniformRandom()<= alpha2 )
		    {
				// don't attach more Ig than the available unbound antigen
				if(pCell->custom_data[nR_EU] >= 1)
				{
					pCell->custom_data[nR_EU] -= 1;
					pCell->custom_data[nR_EB] += 1;
					#pragma omp critical
					{
						pCell->nearest_density_vector()[nAb] -= 1.0 / microenvironment.mesh.dV; 
					}				
				}	
		    }
		}
	}


	return;
}


// this needs to be done on faster time scale
void antigen_antibody_main_model( double dt )
{
	#pragma omp parallel for 
	for( int n=0; n < (*all_cells).size() ; n++ )
	{
		Cell* pC = (*all_cells)[n]; 
		if( pC->phenotype.death.dead == false )
		{ 
			antigen_antibody_dynamics( pC, pC->phenotype , dt ); 
		}
	}

	return;
}


// this function used to handle the antigen and complex value in tumor cell division
void divide_custom_data( double dt )
{

    static double tolerance = 0.001; 
    static int tumor_cell_type = get_cell_definition("tumor cell").type; 
    static double inherit_ratio = parameters.doubles( "antigen_antibody_inherit_ratio" );  // 0-0.5

    #pragma omp parallel for
	for( int i=0; i < (*all_cells).size() ;i++ )	
	{    
        Cell* pCell; 
		pCell = (*all_cells)[i]; 

		static int last_cycle_index = pCell->custom_data.find_variable_index( "last_cycle_entry_time" ); 
		static int generation_index = pCell->custom_data.find_variable_index( "division_generation" );
		static int nR_EU = pCell->custom_data.find_variable_index( "antigen_protein" ); 
	    static int nR_EB = pCell->custom_data.find_variable_index( "antibody_antigen_complex" ); 	
		
		// if cell is dead or not tumor cell, skip it 
		if( pCell->phenotype.death.dead == true || pCell->type != tumor_cell_type )
	    { continue; }
	    
		if( pCell->phenotype.cycle.data.elapsed_time_in_phase < tolerance && 
			fabs( PhysiCell_globals.current_time - pCell->custom_data[ last_cycle_index ] ) >= phenotype_dt ) // 6.0 
		{
			// add generation by 1 
			pCell->custom_data[ generation_index ] += 1;

			// antigen-antibody complex is reset
			pCell->custom_data[ nR_EB ] = floor( inherit_ratio* pCell->custom_data[ nR_EB ] ); 	
			// antigen protein is reset: 500 - complex
			pCell->custom_data[ nR_EU ] = parameters.doubles("original_antigen_protein") - pCell->custom_data[ nR_EB ];  
			
			pCell->custom_data[ last_cycle_index ] = PhysiCell_globals.current_time;
		}           

	}
	
	return; 

} 









