from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark2(IRISHEP_ADLBenchmark):
    """ Plot pT of all jets in all events. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        plots.append(Plot.make1D("jetPt",
            op.map(tree.Jet, lambda j : j.pt), noSel,
            EqBin(100, 15., 60.), title="Jet p_{T} (GeV/c)"))

        return plots
