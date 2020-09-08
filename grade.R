#!/usr/bin/env Rscript
args <- commandArgs(trailing = TRUE)
load(args[1])
load(args[2])
if(all.equal(Std,PMTInfo))
    quit(status=0)
else
    quit(status=1)
