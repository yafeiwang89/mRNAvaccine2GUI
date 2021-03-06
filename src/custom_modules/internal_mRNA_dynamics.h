#include "../core/PhysiCell.h"
#include "../modules/PhysiCell_standard_modules.h" 

using namespace BioFVM; 
using namespace PhysiCell;

#include "./submodel_data_structures.h" 

#ifndef __internal_mRNA_dynamics__
#define __internal_mRNA_dynamics__

extern Submodel_Information internal_mRNA_dynamics_info; 
	
void internal_mRNA_model_setup( void );

void internal_mRNA_model( Cell* pCell, Phenotype& phenotype, double dt );

#endif 