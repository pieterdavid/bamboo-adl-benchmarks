""" Base module for histograms based on CMS open data (using the NanoAOD decorators) """

from bamboo.analysismodules import NanoAODHistoModule
import bamboo.logging
logger = bamboo.logging.getLogger(__name__)
import os.path

class IRISHEP_ADLBenchmark(NanoAODHistoModule):
    def addArgs(self, parser):
        super(IRISHEP_ADLBenchmark, self).addArgs(parser)
        parser.add_argument("--prefix", type=str, default="test_", help="Prefix for output pngs")
    def postProcess(self, taskList, config=None, workdir=None, resultsdir=None):
        ## no plotIt, just a png of the individual histograms (single sample)
        logger.info("The resulting histograms are stored in the {0} directory, plots will be in {1}".format(resultsdir, workdir))
        for i,((inputs, outputFile), kwargs) in enumerate(taskList):
            outputFile = os.path.join(resultsdir, outputFile)
            if len(taskList) != 1:
                prefix = "{0}{1}_".format(self.args.prefix, kwargs.get("sample", str(i)))
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
