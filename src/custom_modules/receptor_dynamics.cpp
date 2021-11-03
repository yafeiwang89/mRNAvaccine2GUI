#include "./receptor_dynamics.h" 

using namespace PhysiCell; 

std::string receptor_model_version = "0.2.0"; 

Submodel_Information receptor_dynamics_info; 

void receptor_dynamics_model_setup( void )
{
		// set version 
	receptor_dynamics_info.name = "receptor dynamics"; 
	receptor_dynamics_info.version = receptor_model_version; 
		// set functions 
	receptor_dynamics_info.main_function = receptor_dynamics_main_model; 
	receptor_dynamics_info.phenotype_function = NULL; // pushed into the "main" model  
	receptor_dynamics_info.mechanics_function = NULL; 	
		// what microenvironment variables do you need 

		// what cell variables and parameters do you need? 

	receptor_dynamics_info.cell_variables.push_back( "endosome_LNP" ); 

	receptor_dynamics_info.cell_variables.push_back( "unbound_external_receptor" ); 
	receptor_dynamics_info.cell_variables.push_back( "bound_external_receptor" ); 
	receptor_dynamics_info.cell_variables.push_back( "unbound_internal_receptor" ); 
	receptor_dynamics_info.cell_variables.push_back( "bound_internal_receptor" ); 
	
	receptor_dynamics_info.cell_variables.push_back( "receptor_binding_rate" ); 
	receptor_dynamics_info.cell_variables.push_back( "receptor_endocytosis_rate" ); 
	receptor_dynamics_info.cell_variables.push_back( "receptor_cargo_release_rate" ); 	
	receptor_dynamics_info.cell_variables.push_back( "receptor_recycling_rate" ); 
	
	// submodel_registry.register_model( receptor_dynamics_info ); 
	receptor_dynamics_info.register_model(); 
	
	return; 
}

void receptor_dynamics_model( Cell* pCell, Phenotype& phenotype, double dt )
{
	
	static int DC_type = get_cell_definition( "DC" ).type; 
	
	// bookkeeping -- find microenvironment variables we need
	static int LNP_external = microenvironment.find_density_index( "Lipid-nanoparticles" ); 
	static int LNP_endosome = pCell->custom_data.find_variable_index( "endosome_LNP" ); 
	static int LNP_all = pCell->custom_data.find_variable_index( "total_intern_LNP" ); 

	static double LNP_saturation = 5; // LNPs saturation value in DCs 


	// bookkeeping -- find custom data we need 
	
	static int nR_EU = pCell->custom_data.find_variable_index( "unbound_external_receptor" ); 
	static int nR_EB = pCell->custom_data.find_variable_index( "bound_external_receptor" ); 
	static int nR_IU = pCell->custom_data.find_variable_index( "unbound_internal_receptor" ); 
	static int nR_IB = pCell->custom_data.find_variable_index( "bound_internal_receptor" ); 
	
	static int nR_bind = pCell->custom_data.find_variable_index( "receptor_binding_rate" ); 
	static int nR_endo = pCell->custom_data.find_variable_index( "receptor_endocytosis_rate" ); 
	static int nR_release = pCell->custom_data.find_variable_index( "receptor_cargo_release_rate" ); 	
	static int nR_recycle = pCell->custom_data.find_variable_index( "receptor_recycling_rate" ); 


	// do nothing if dead 
	if( phenotype.death.dead == true )
	{ return; } 

	// if not Dendritic cell, do nothing         
	if( pCell->type != DC_type )
	{ return; } 

	// actual model goes here 


	// let's use stochastic binding process instead now
/*  
	// internalized LNP tells us how many have recently bound to receptors 
	double newly_bound = phenotype.molecular.internalized_total_substrates[LNP_external]; 

	// if it tried to bind to more LNP than there are receptors, compensate 
	double excess_binding = newly_bound - pCell->custom_data[nR_EU]; 
	if( excess_binding > 0.0 )
	{
		// don't bring in more LNP than there are receptors 
		newly_bound = pCell->custom_data[nR_EU]; 
		// dump any excess back into the microenvironment
		static double one_LNP_to_density = 1.0 / microenvironment.mesh.dV; 
		// this needs omp critical because 2 cells writing to 1 voxel is not thread safe 
		#pragma omp critical
		{
			pCell->nearest_density_vector()[LNP_external] += excess_binding * one_LNP_to_density; 
		}
	}

	// record all endocytosis LNP 
	pCell->custom_data[ LNP_all ] += newly_bound; 

	phenotype.molecular.internalized_total_substrates[LNP_external] = 0.0; 
	
	// add newly bound receptor to R_EB	
	pCell->custom_data[nR_EB] += newly_bound; 
	
	// remove newly bound receptor from R_EU 
	pCell->custom_data[nR_EU] -= newly_bound; 
*/


    // dt*r_bind *rho* V_cell *R_EU,  rho is possible negative
    double dt_bind = dt* pCell->custom_data[nR_bind]* pCell->nearest_density_vector()[LNP_external]*
     					phenotype.volume.total* pCell->custom_data[nR_EU]* (1- pCell->custom_data[LNP_all]/LNP_saturation );

	if( dt_bind>0 && dt_bind<1 )
	{
		if( UniformRandom()<= dt_bind )
		{
			// don't attach more LNPs than the available unbound receptor
			if(pCell->custom_data[nR_EU] >= 1)
			{
				pCell->custom_data[nR_EU] -= 1;
				pCell->custom_data[nR_EB] += 1;
				// record all endocytosis LNP 
				pCell->custom_data[ LNP_all ] += 1; 
				// negative ??
				#pragma omp critical
				{
					pCell->nearest_density_vector()[LNP_external] -= 1.0 / microenvironment.mesh.dV; 
				}    
			}
			/*
			else
			{
				pCell->custom_data[nR_EB] += pCell->custom_data[nR_EU];
				pCell->custom_data[nR_EU] = 0;
			}
			*/		
		}
	}

	if( dt_bind >=1 )
	{
		double n_LNP = pCell->nearest_density_vector()[LNP_external]* phenotype.volume.total;
		// minimum( rh0*V_voxel, R_EU )
		// if(n_LNP > pCell->custom_data[nR_EU])
		// { n_LNP = pCell->custom_data[nR_EU]; }
        double alpha = dt_bind;
        
        // make sure LNPs around cell >= dt_bind
        if(alpha > n_LNP)
        {
        	alpha = n_LNP;
        }


	    double alpha1 = floor( alpha );
	    double alpha2 = alpha - alpha1;

        // don't attach more LNPs than the available unbound receptor
        if(alpha1 > pCell->custom_data[nR_EU])
        {
        	alpha1 = pCell->custom_data[nR_EU];
        }
        pCell->custom_data[nR_EU] -= alpha1;
		pCell->custom_data[nR_EB] += alpha1;
		pCell->custom_data[ LNP_all ] += alpha1;
		#pragma omp critical
		{
			pCell->nearest_density_vector()[LNP_external] -= alpha1 / microenvironment.mesh.dV;
		}
	        
	    if( UniformRandom()<= alpha2 )
	    {
			// don't attach more LNPs than the available unbound receptor
			if(pCell->custom_data[nR_EU] >= 1)
			{
				pCell->custom_data[nR_EU] -= 1;
				pCell->custom_data[nR_EB] += 1;
				pCell->custom_data[ LNP_all ] += 1;
				#pragma omp critical
				{
					pCell->nearest_density_vector()[LNP_external] -= 1.0 / microenvironment.mesh.dV; 
				}
				
			}	
			/*
			else
			{
				pCell->custom_data[nR_EB] += pCell->custom_data[nR_EU];
				pCell->custom_data[nR_EU] = 0;
			}
			*/		
	    }
	}


    // make sure endocytosis at most <LNP_saturation> LNPs !!!!!

    double excess_binding = pCell->custom_data[ LNP_all ] - LNP_saturation; 

    if( excess_binding > 0.0 )
    {
 		pCell->custom_data[nR_EU] += excess_binding;
		pCell->custom_data[nR_EB] -= excess_binding;
    	pCell->custom_data[ LNP_all ] = LNP_saturation;
    	#pragma omp critical
		{
			pCell->nearest_density_vector()[LNP_external] += excess_binding / microenvironment.mesh.dV;
		}
    }

    if (pCell->custom_data[nR_EB] < 0.0 )
    {
    	pCell->custom_data[nR_EB] = 0;
    }

	
	// endocytosis 
	
	double dR_IB = dt*pCell->custom_data[nR_endo]*pCell->custom_data[nR_EB];
	if( dR_IB > pCell->custom_data[nR_EB] )
	{ dR_IB = pCell->custom_data[nR_EB]; }
	pCell->custom_data[nR_EB] -= dR_IB; // move from external bound
	pCell->custom_data[nR_IB] += dR_IB; // move to internal bound
	
	// LNPs release from endosomes 
	
	double dR_IU = dt*pCell->custom_data[nR_release]*pCell->custom_data[nR_IB];
	if( dR_IU > pCell->custom_data[nR_IB] )
	{ dR_IU = pCell->custom_data[nR_IB]; }
	pCell->custom_data[nR_IB] -= dR_IU; // move from internal bound 
	pCell->custom_data[nR_IU] += dR_IU; // move to internal unbound 
	pCell->custom_data[LNP_endosome] += dR_IU; // release LNP in the endosome 
	
	// receptor recycling 
	
	double dR_EU = dt*pCell->custom_data[nR_recycle]*pCell->custom_data[nR_IU];
	if( dR_EU > pCell->custom_data[nR_IU] )
	{ dR_EU = pCell->custom_data[nR_IU]; }
	pCell->custom_data[nR_IU] -= dR_EU; // move from internal unbound 
	pCell->custom_data[nR_EU] += dR_EU; // move to external unbound 
	

	// update the LNP uptake rate, this needs to be modified based on nanobio project !!!!
	// NOT NEED NOW !!!
	// phenotype.secretion.uptake_rates[LNP_external] = pCell->custom_data[nR_bind] 
	// 	*pCell->custom_data[nR_EU]* (1- pCell->custom_data[LNP_all]/LNP_saturation );  // r0* (1- LNP_intern/LNP_saturation)

	
	return; 
}

void receptor_dynamics_main_model( double dt )
{
	static bool flag_LNP_initial = parameters.bools( "encapsulate_LNP_initial" );

	// If directly encapsulate LNPs in endosome of DC cells directly, no need call this function
	if( flag_LNP_initial == true)
	{
		return; 
	}

	#pragma omp parallel for 
	for( int n=0; n < (*all_cells).size() ; n++ )
	{
		Cell* pC = (*all_cells)[n]; 
		if( pC->phenotype.death.dead == false )
		{ receptor_dynamics_model( pC, pC->phenotype , dt ); }
	}
	
	return; 
}
	
