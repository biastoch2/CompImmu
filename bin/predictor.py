#!/usr/bin/env python
import argparse
import sys
sys.path.append('../')
sys.path.append('../feature_extractors')
from scikit_predictor import ScikitPredictor
from data import Data
from amino_acids import AminoAcids
from bin9 import Bin9
from blo_dist import BloDist
from char6 import Char6
from data import Data
from ic50 import IC50
from misc import Misc

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description = "Epitope Binding Predictor")
  parser.add_argument('input',metavar='in-file')
  parser.add_argument('output', metavar='out-file')
  args = parser.parse_args()

  # Load previously trained classifier from disk 
  pred = ScikitPredictor()
  features = pred.loadTrainedClassifier('featureset_PhysProperties__solver_sgd-hidden_layer_sizes_(30, 10)-learning_rate_init_0.01-momentum_0.1-activation_tanh.pkl')
  d = Data().setFeatures(features)
  
  print("Using '"+features.__class__.__name__+"' featureset.")

  with open(args.output, "w") as o:
    with open(args.input, "r") as i:
      for e in i:
        peptide = e.strip()
      
        # Populate Data-Object with peptides and add same Feature extractors as used when training the classifier
        d.loadFromArray([peptide])

        # Get Features of peptides as arrays 
        peptid_features = d.toFeatureArray()

        is_binder = pred.classify(peptid_features)
      
        o.write("%s\t%i\n"%(peptide,is_binder))

