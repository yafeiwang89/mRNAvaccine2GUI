/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

void create_cell_types( void )
{
	// set the random seed 
	SeedRandom( parameters.ints("random_seed") );  
	
	/* 
	   Put any modifications to default cell definition here if you 
	   want to have "inherited" by other cell types. 
	   
	   This is a good place to set default functions. 
	*/ 
	cell_defaults.functions.volume_update_function = standard_volume_update_function;
	cell_defaults.functions.update_velocity = standard_update_cell_velocity;

	cell_defaults.functions.update_migration_bias = NULL; 
	cell_defaults.functions.update_phenotype = NULL;  
	cell_defaults.functions.custom_cell_rule = NULL; 
	
	cell_defaults.functions.add_cell_basement_membrane_interactions = NULL; 
	cell_defaults.functions.calculate_distance_to_membrane = NULL; 
	
	
	/*
	   This parses the cell definitions in the XML config file. 
	*/
	
	initialize_cell_definitions_from_pugixml(); 

	/* 
	   Put any modifications to individual cell definitions here. 
	   
	   This is a good place to set custom functions. 
	*/ 
	
	// register the submodels 
	// (which ensures that the cells have all the internal variables they need) 

	static int LNP_index = microenvironment.find_density_index( "Lipid-nanoparticles" ); 
	
	Cell_Definition* pCD = find_cell_definition( "DC" ); 
	pCD->phenotype.molecular.fraction_released_at_death[LNP_index] = 
		parameters.doubles("LNP_fraction_released_at_death"); 

	
	immune_submodels_setup();

	DC_LNP_mRNA_model_setup(); 

	// receptor_dynamics_model_setup(); 
	// internal_virus_model_setup();
	// internal_virus_response_model_setup();
	
	// not use in vaccine project
	// epithelium_submodel_setup(); 

	tumor_submodel_setup();


	submodel_registry.display( std::cout ); 
		
	/*
	   This builds the map of cell definitions and summarizes the setup. 
	*/
		
	build_cell_definitions_maps(); 
	display_cell_definitions( std::cout ); 
	
	return; 
}

void setup_microenvironment( void )
{
	// set domain parameters 
	
/* now this is in XML 
	default_microenvironment_options.X_range = {-1000, 1000}; 
	default_microenvironment_options.Y_range = {-1000, 1000}; 
	default_microenvironment_options.simulate_2D = true; 
*/
	
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
/* now this is in XML 	
	// no gradients need for this example 

	default_microenvironment_options.calculate_gradients = false; 
	
	// set Dirichlet conditions 

	default_microenvironment_options.outer_Dirichlet_conditions = true;
	
	// if there are more substrates, resize accordingly 
	std::vector<double> bc_vector( 1 , 38.0 ); // 5% o2
	default_microenvironment_options.Dirichlet_condition_vector = bc_vector;
	
	// set initial conditions 
	default_microenvironment_options.initial_condition_vector = { 38.0 }; 
*/
	
	// put any custom code to set non-homogeneous initial conditions or 
	// extra Dirichlet nodes here. 
	
	// initialize BioFVM 
	
	initialize_microenvironment(); 	
	
	return; 
}

void setup_tissue( void )
{
	
	choose_initialized_voxels();
	
	// hexagonal cell packing 
	Cell_Definition* pCD = find_cell_definition("tumor cell"); 
	
	double cell_radius = pCD->phenotype.geometry.radius; 
	double cell_spacing = 0.95 * 2.0 * cell_radius; 
	
	double tumor_radius = parameters.doubles( "tumor_radius" ); // 250
	
	Cell* pCell = NULL; 
	
	double center_x = 0.5*(  microenvironment.mesh.bounding_box[0] + microenvironment.mesh.bounding_box[3] );
	double center_y = 0.5*(  microenvironment.mesh.bounding_box[1] + microenvironment.mesh.bounding_box[4] );
	
	double x = 0; 
	double x_outer =  tumor_radius; 
	double y = 0; 
	
	int n = 0; 
	while( y < tumor_radius )
	{
		x = 0; 
		if( n % 2 == 1 )
		{ x = 0.5*cell_spacing; }
		x_outer = sqrt( tumor_radius*tumor_radius - y*y ); 
		
		while( x < x_outer )
		{
			pCell = create_cell( get_cell_definition("tumor cell") ); // tumor cell 
			pCell->assign_position( center_x+x , center_y+y , 0.0 );
		
			if( fabs( y ) > 0.01 )
			{
				pCell = create_cell( get_cell_definition("tumor cell") ); // tumor cell 
				pCell->assign_position( center_x+x , center_y-y , 0.0 );
			}
			
			if( fabs( x ) > 0.01 )
			{ 
				pCell = create_cell( get_cell_definition("tumor cell") ); // tumor cell 
				pCell->assign_position( center_x-x , center_y+y , 0.0 );
			
				if( fabs( y ) > 0.01 )
				{
					pCell = create_cell( get_cell_definition("tumor cell") ); // tumor cell 
					pCell->assign_position( center_x-x , center_y-y , 0.0 );
				}
			}
			x += cell_spacing; 	
		}
		
		y += cell_spacing * sqrt(3.0)/2.0; 
		n++; 
	}


	// set DC cells in main loop
	// introduce_DC_cells(); 

	// not use in vaccine project now
	// now place immune cells 
	// initial_immune_cell_placement();
	
	return; 
}


std::vector<std::string> tumor_coloring_function( Cell* pCell )
{
	std::vector<std::string> output( 4, "blue" ); 

	// color by antigen-antibody complex  
	static int color_index = pCell->custom_data.find_variable_index( "antibody_antigen_complex" ); 
	static double Ig_c = parameters.doubles( "max_Ig_complex_color" ); 
		
	if( pCell->phenotype.death.dead == false )
	{
		// find tumor cell's antigen-antibody complex 
		double v = pCell->custom_data[ color_index ] ; 
		double interpolation = 0; 
		
		if( v < 0.01*Ig_c )
		{ interpolation = 0; } 

		if( v >= 0.01*Ig_c && v < 0.1*Ig_c )
		{ interpolation = 0.1; } 

		if( v >= 0.1*Ig_c && v < 0.25*Ig_c )
		{ interpolation = 0.25; } 

		if( v >= 0.25*Ig_c && v < 0.5*Ig_c )
		{ interpolation = 0.5; } 

		if( v >= 0.5*Ig_c && v < 0.75*Ig_c )
		{ interpolation = 0.75; } 

		if( v >= 0.75*Ig_c )
		{ interpolation = 1.0; } 

		int red = (int) floor( 255.0 * interpolation ) ; 
		int green = red; 
		int blue = 255 - red; 

		char color [1024]; 
		sprintf( color, "rgb(%u,%u,%u)" , red,green,blue ); 

		output[0] = color; 
		output[2] = color; 
		output[3] = color; 
	}
	
	return output; 
}


std::string blue_yellow_interpolation( double min, double val, double max )
{
// 	std::string out;
	
	double interpolation = (val-min)/(max-min+1e-16); 
	if( interpolation < 0.0 )
	{ interpolation = 0.0; } 
	if( interpolation > 1.0 )
	{ interpolation = 1.0; }
	
	int red_green = (int) floor( 255.0 * interpolation ) ; 
	int blue = 255 - red_green; 

	char color [1024]; 
	sprintf( color, "rgb(%u,%u,%u)" , red_green,red_green,blue ); 
	return color;  
}

std::vector<std::string> tissue_coloring_function( Cell* pCell )
{
	static int tumor_cell_type = get_cell_definition( "tumor cell" ).type; 
	
	static int CD8_Tcell_type = get_cell_definition( "CD8 Tcell" ).type; 
	static int Macrophage_type = get_cell_definition( "macrophage" ).type; 
	static int DC_type = get_cell_definition( "DC" ).type; 
	static int CD4_Tcell_type = get_cell_definition( "CD4 Tcell" ).type;  
	
	// start with white 
	
	std::vector<std::string> output = {"white", "black", "white" , "white" };	
	// false_cell_coloring_cytometry(pCell); 

	// tumor cell 
	if ( pCell->phenotype.death.dead == true && pCell->type == tumor_cell_type)
	{
		// Apoptotic - black
		if (pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::apoptotic)  
		{
			output[0] = parameters.strings("apoptotic_tumor_color");	
			output[2] = output[0];
			output[3] = output[0];
			return output; 
		}
		// Necrotic - grey, as CD4+ is brown in mRNA vaccine project
		if( pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_swelling || 
			pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_lysed || 
			pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic )
		{
			output[0] = "rgb(47,79,79)";  // rgb(250,138,38)  (Brown)
			output[2] = output[0];
			output[3] = output[0];
			return output;
		}
	}	

	if( pCell->phenotype.death.dead == false && pCell->type == tumor_cell_type )
	{
		// color by antigen-antibody complex  
		output = tumor_coloring_function(pCell); 
		return output; 
	}

	
	// immune cells 
	if( pCell->phenotype.death.dead == true && pCell->type != tumor_cell_type)
	{
		output[0] = parameters.strings("apoptotic_immune_color");		
		output[2] = output[0]; 		
		output[3] = output[0]; 	
		return output; 
	}
	
	if( pCell->phenotype.death.dead == false && pCell->type == CD8_Tcell_type )
	{
		output[0] = parameters.strings("CD8_Tcell_color");  
		output[2] = output[0];
		output[3] = output[0];
		return output; 
	}
	
	// (Adrianne) adding CD4 T cell colouring
	if( pCell->phenotype.death.dead == false && pCell->type == CD4_Tcell_type )
	{
		output[0] = parameters.strings("CD4_Tcell_color");  
		output[2] = output[0];
		output[3] = output[0];
		return output; 
	}

	if( pCell->phenotype.death.dead == false && pCell->type == Macrophage_type )
	{
		std::string color = parameters.strings("Macrophage_color");  
		if( pCell->custom_data["activated_immune_cell" ] > 0.5 )
		{ color = parameters.strings("activated_macrophage_color"); }
		
		// (Adrianne) added colours to show when macrophages are exhausted and when they are hyperactivated
		if( pCell->phenotype.volume.total> pCell->custom_data["threshold_macrophage_volume"] )// macrophage exhausted
		{ color = parameters.strings("exhausted_macrophage_color"); }
		else if( pCell->custom_data["ability_to_phagocytose_infected_cell"] == 1)// macrophage has been activated to kill infected cells by T cell
		{ color = parameters.strings("hyperactivated_macrophage_color"); }
		
		output[0] = color; 
		output[2] = output[0];
		output[3] = output[0];
		return output; 
	}
	
	//(Adrianne) adding colour for DCs
	if( pCell->phenotype.death.dead == false && pCell->type == DC_type )
	{
		std::string color = parameters.strings("DC_color");  
		if( pCell->custom_data["activated_immune_cell" ] > 0.5 )
		{ color = parameters.strings("activated_DC_color"); }
	
		output[0] = color; 
		output[2] = output[0];
		output[3] = output[0];
		return output; 
	}

	return output; 
}


bool Write_SVG_circle_opacity( std::ostream& os, double center_x, double center_y, double radius, double stroke_size, 
                       std::string stroke_color , std::string fill_color , double opacity )
{
 os << "  <circle cx=\"" << center_x << "\" cy=\"" << center_y << "\" r=\"" << radius << "\" stroke-width=\"" << stroke_size 
    << "\" stroke=\"" << stroke_color << "\" fill=\"" << fill_color 
	<< "\" fill-opacity=\"" << opacity << "\"/>" << std::endl; 
 return true; 
}


//
void SVG_plot_virus( std::string filename , Microenvironment& M, double z_slice , double time, std::vector<std::string> (*cell_coloring_function)(Cell*) )
{
	static double X_lower = M.mesh.bounding_box[0];
	static double X_upper = M.mesh.bounding_box[3];
 
	static double Y_lower = M.mesh.bounding_box[1]; 
	static double Y_upper = M.mesh.bounding_box[4]; 

	static double plot_width = X_upper - X_lower; 
	static double plot_height = Y_upper - Y_lower; 

	static double font_size = 0.025 * plot_height; // PhysiCell_SVG_options.font_size; 
	static double top_margin = font_size*(.2+1+.2+.9+.5 ); 
	
	static double epithelial_opacity = parameters.doubles("epithelial_opacity");
	static double non_epithelial_opacity = parameters.doubles("non_epithelial_opacity"); 

	// open the file, write a basic "header"
	std::ofstream os( filename , std::ios::out );
	if( os.fail() )
	{ 
		std::cout << std::endl << "Error: Failed to open " << filename << " for SVG writing." << std::endl << std::endl; 

		std::cout << std::endl << "Error: We're not writing data like we expect. " << std::endl
		<< "Check to make sure your save directory exists. " << std::endl << std::endl
		<< "I'm going to exit with a crash code of -1 now until " << std::endl 
		<< "you fix your directory. Sorry!" << std::endl << std::endl; 
		exit(-1); 
	} 
	
	Write_SVG_start( os, plot_width , plot_height + top_margin );

	// draw the background 
	Write_SVG_rect( os , 0 , 0 , plot_width, plot_height + top_margin , 0.002 * plot_height , "white", "white" );

	// write the simulation time to the top of the plot
 
	char* szString; 
	szString = new char [1024]; 
 
	int total_cell_count = all_cells->size(); 
 
	double temp_time = time; 

	std::string time_label = formatted_minutes_to_DDHHMM( temp_time ); 
 
	sprintf( szString , "Current time: %s, z = %3.2f %s", time_label.c_str(), 
		z_slice , PhysiCell_SVG_options.simulation_space_units.c_str() ); 
	Write_SVG_text( os, szString, font_size*0.5,  font_size*(.2+1), 
		font_size, PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	sprintf( szString , "%u agents" , total_cell_count ); 
	Write_SVG_text( os, szString, font_size*0.5,  font_size*(.2+1+.2+.9), 
		0.95*font_size, PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	
	delete [] szString; 


	// add an outer "g" for coordinate transforms 
	
	os << " <g id=\"tissue\" " << std::endl 
	   << "    transform=\"translate(0," << plot_height+top_margin << ") scale(1,-1)\">" << std::endl; 
	   
	// prepare to do mesh-based plot (later)
	
	double dx_stroma = M.mesh.dx; 
	double dy_stroma = M.mesh.dy; 
	
	os << "  <g id=\"ECM\">" << std::endl; 
  
	int ratio = 1; 
	double voxel_size = dx_stroma / (double) ratio ; 
  
	double half_voxel_size = voxel_size / 2.0; 
	double normalizer = 78.539816339744831 / (voxel_size*voxel_size*voxel_size); 
 
 // color in the background ECM
/* 
 if( ECM.TellRows() > 0 )
 {
  // find the k corresponding to z_slice
  
  
  
  Vector position; 
  *position(2) = z_slice; 
  

  // 25*pi* 5 microns^2 * length (in source) / voxelsize^3
  
  for( int j=0; j < ratio*ECM.TellCols() ; j++ )
  {
   // *position(1) = *Y_environment(j); 
   *position(1) = *Y_environment(0) - dy_stroma/2.0 + j*voxel_size + half_voxel_size; 
   
   for( int i=0; i < ratio*ECM.TellRows() ; i++ )
   {
    // *position(0) = *X_environment(i); 
    *position(0) = *X_environment(0) - dx_stroma/2.0 + i*voxel_size + half_voxel_size; 
	
    double E = evaluate_Matrix3( ECM, X_environment , Y_environment, Z_environment , position );	
	double BV = normalizer * evaluate_Matrix3( OxygenSourceHD, X_environment , Y_environment, Z_environment , position );
	if( isnan( BV ) )
	{ BV = 0.0; }

	vector<string> Colors;
	Colors = hematoxylin_and_eosin_stroma_coloring( E , BV );
	Write_SVG_rect( os , *position(0)-half_voxel_size-X_lower , *position(1)-half_voxel_size+top_margin-Y_lower, 
	voxel_size , voxel_size , 1 , Colors[0], Colors[0] );
   
   }
  }
 
 }
*/
	os << "  </g>" << std::endl; 
	
	// static Cell_Definition* pEpithelial = find_cell_definition( "lung epithelium" ); 
 
	// plot intersecting epithelial cells 
	os << "  <g id=\"cells\">" << std::endl; 


	
	// plot intersecting non=epithelial cells 
	for( int i=0 ; i < total_cell_count ; i++ )
	{
		Cell* pC = (*all_cells)[i]; // global_cell_list[i]; 
  
		static std::vector<std::string> Colors; 
		if( fabs( (pC->position)[2] - z_slice ) < pC->phenotype.geometry.radius)
		{
			double r = pC->phenotype.geometry.radius ; 
			double rn = pC->phenotype.geometry.nuclear_radius ; 
			double z = fabs( (pC->position)[2] - z_slice) ; 
   
			Colors = cell_coloring_function( pC ); 

			os << "   <g id=\"cell" << pC->ID << "\">" << std::endl; 
  
			// figure out how much of the cell intersects with z = 0 
   
			double plot_radius = sqrt( r*r - z*z ); 

			Write_SVG_circle_opacity( os, (pC->position)[0]-X_lower, (pC->position)[1]-Y_lower, 
				plot_radius , 0.5, Colors[1], Colors[0] , non_epithelial_opacity ); 
/*
			// plot the nucleus if it, too intersects z = 0;
			if( fabs(z) < rn && PhysiCell_SVG_options.plot_nuclei == true )
			{   
				plot_radius = sqrt( rn*rn - z*z ); 
			 	Write_SVG_circle( os, (pC->position)[0]-X_lower, (pC->position)[1]-Y_lower, 
					plot_radius, 0.5, Colors[3],Colors[2]); 
			}		
*/			
			os << "   </g>" << std::endl;
		}
		
	}
	
	os << "  </g>" << std::endl; 
	
	// plot intersecting BM points
	/* 
	 for( int i=0 ; i < BasementMembraneNodes.size() ; i++ )
	 {
		// vector<string> Colors = false_cell_coloring( pC ); 
		BasementMembraneNode* pBMN = BasementMembraneNodes[i]; 
		double thickness =0.1; 
		
		if( fabs( *(pBMN->Position)(2) - z_slice ) < thickness/2.0 ) 
		{
		 string bm_color ( "rgb(0,0,0)" );
		 double r = thickness/2.0; 
		 double z = fabs( *(pBMN->Position)(2) - z_slice) ; 

		 os << " <g id=\"BMN" << pBMN->ID << "\">" << std::endl; 
		 Write_SVG_circle( os,*(pBMN->Position)(0)-X_lower, *(pBMN->Position)(1)+top_margin-Y_lower, 10*thickness/2.0 , 0.5 , bm_color , bm_color ); 
		 os << " </g>" << std::endl;
		}
		// pC = pC->pNextCell;
	 }
	*/ 
	
	// end of the <g ID="tissue">
	os << " </g>" << std::endl; 
 
	// draw a scale bar
 
	double bar_margin = 0.025 * plot_height; 
	double bar_height = 0.01 * plot_height; 
	double bar_width = PhysiCell_SVG_options.length_bar; 
	double bar_stroke_width = 0.001 * plot_height; 
	
	std::string bar_units = PhysiCell_SVG_options.simulation_space_units; 
	// convert from micron to mm
	double temp = bar_width;  

	if( temp > 999 && std::strstr( bar_units.c_str() , PhysiCell_SVG_options.mu.c_str() )   )
	{
		temp /= 1000;
		bar_units = "mm";
	}
	// convert from mm to cm 
	if( temp > 9 && std::strcmp( bar_units.c_str() , "mm" ) == 0 )
	{
		temp /= 10; 
		bar_units = "cm";
	}
	
	szString = new char [1024];
	sprintf( szString , "%u %s" , (int) round( temp ) , bar_units.c_str() );
 
	Write_SVG_rect( os , plot_width - bar_margin - bar_width  , plot_height + top_margin - bar_margin - bar_height , 
		bar_width , bar_height , 0.002 * plot_height , "rgb(255,255,255)", "rgb(0,0,0)" );
	Write_SVG_text( os, szString , plot_width - bar_margin - bar_width + 0.25*font_size , 
		plot_height + top_margin - bar_margin - bar_height - 0.25*font_size , 
		font_size , PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() ); 
	
	delete [] szString; 

	// plot runtime 
	szString = new char [1024]; 
	RUNTIME_TOC(); 
	std::string formatted_stopwatch_value = format_stopwatch_value( runtime_stopwatch_value() );
	Write_SVG_text( os, formatted_stopwatch_value.c_str() , bar_margin , top_margin + plot_height - bar_margin , 0.75 * font_size , 
		PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	delete [] szString; 

	// draw a box around the plot window
	Write_SVG_rect( os , 0 , top_margin, plot_width, plot_height , 0.002 * plot_height , "rgb(0,0,0)", "none" );
	
	// close the svg tag, close the file
	Write_SVG_end( os ); 
	os.close();
 
	return; 
}


