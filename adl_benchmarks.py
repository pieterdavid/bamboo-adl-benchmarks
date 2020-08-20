""" Base module for histograms based on CMS open data (using the NanoAOD decorators) """

from bamboo.analysismodules import NanoAODHistoModule
import bamboo.logging
logger = bamboo.logging.getLogger(__name__)
import os.path

from bamboo.treedecorators import NanoAODDescription
description_CMSRun1OpenData_ROOTbenchmark = NanoAODDescription(groups=["HLT_", "PV_", "MET_"], collections=["nMuon", "nElectron", "nTau", "nPhoton", "nJet"])

class IRISHEP_ADLBenchmark(NanoAODHistoModule):
    def addArgs(self, parser):
        super(IRISHEP_ADLBenchmark, self).addArgs(parser)
        parser.add_argument("--prefix", type=str, default="test_", help="Prefix for output pngs")
    def prepareTree(self, tree, sample=None, sampleCfg=None):
        return super(IRISHEP_ADLBenchmark, self).prepareTree(tree, sample=sample, sampleCfg=sampleCfg, description=description_CMSRun1OpenData_ROOTbenchmark)
    def postProcess(self, taskList, config=None, workdir=None, resultsdir=None):
        ## no plotIt, just a png of the individual histograms (single sample)
        logger.info("The resulting histograms are stored in the {0} directory, plots will be in {1}".format(resultsdir, workdir))
        for i,task in enumerate(taskList):
            outputFile = os.path.join(resultsdir, task.outputFile)
            if len(taskList) != 1:
                prefix = "{0}{1}_".format(self.args.prefix, task.name)
            else:
                prefix = self.args.prefix
            from bamboo.root import gbl
            f = gbl.TFile.Open(outputFile)
            if not f:
                raise RuntimeError("Could not open file {0}".format(outputFile))
            for j,ky in enumerate(f.GetListOfKeys()):
                obj = f.Get(ky.GetName())
                if not obj:
                    raise RuntimeError("Could not get object {0} from file {1}".format(ky.GetName(), outputFile))
                if ky.GetClassName() in ("TH1F", "TH1D", "TH2F"):
                    cv = gbl.TCanvas("c{0:d}_{1}".format(j, prefix))
                    if ky.GetClassName() == "TH2F":
                        obj.Draw("COLZ")
                    else:
                        obj.Draw()
                    cv.Update()
                    cv.SaveAs(os.path.join(workdir, "{0}{1}.png".format(prefix, ky.GetName())))
    def mergeCounters(self, outF, infileNames, sample=None):
        pass ## disabled because the test file is not a full NanoAOD
