from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark3(IRISHEP_ADLBenchmark):
    """ Plot pT of jets with |η| < 1. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        centralJets1 = op.select(tree.Jet, lambda j : op.abs(j.eta) < 1.)
        plots.append(Plot.make1D("central1_jetPt",
            op.map(centralJets1, lambda j : j.pt), noSel,
            EqBin(100, 15., 60.), title="Jet p_{T} (GeV/c)"))

        return plots
