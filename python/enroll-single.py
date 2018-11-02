##-----------------------------------------------------------------------------
##  Author      : Thuy Nguyen-Chinh
##  Date        : Nov 23, 2017
##
##  Interpreter : Python 3.5
##  Description : Enroll an account
##-----------------------------------------------------------------------------


##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import argparse, os
from time import time
import scipy.io as sio

from fnc.extractFeature import extractFeature
from path import temp_database_path


#------------------------------------------------------------------------------
#	Argument parsing
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str,
                    help="Path to the file that you want to verify.")

parser.add_argument("--temp_dir", type=str, default="./templates/",
					help="Path to the directory containing templates.")

args = parser.parse_args()


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
start = time()

# Extract feature
print('>>> Enroll for the file ', args.file)
template, mask, file = extractFeature(args.file)

# Save extracted feature
basename = os.path.basename(file)
out_file = os.path.join(temp_database_path, "%s.mat" % (basename))
sio.savemat(out_file, mdict={'template':template, 'mask':mask})
print('>>> Template is saved in %s' % (out_file))

end = time()
print('>>> Enrollment time: {} [s]\n'.format(end-start))