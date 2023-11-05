#!/bin/bash -x

cd $(dirname $0)

brew tap twilio/brew && brew install twilio

source ./install-twilio-prerequisites-python.sh
