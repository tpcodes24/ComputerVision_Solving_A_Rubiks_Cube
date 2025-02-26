from rubikscubetracker import RubiksVideo
import argparse
import logging
import os
import sys
import subprocess

# Logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)22s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Command line args
parser = argparse.ArgumentParser("Rubiks Square Extractor")
parser.add_argument('-w', '--webcam', type=int, default=None, help='webcam to use...0, 1, etc')
args = parser.parse_args()

if args.webcam is None and args.directory is None and args.filename is None:
    log.error("args.directory and args.filename are None")
    sys.exit(1)

if args.webcam is not None:
    rvid = RubiksVideo(args.webcam)
    rvid.analyze_webcam()
