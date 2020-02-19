from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark1(IRISHEP_ADLBenchmark):
    """ Plot the missing ET of all events. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin

        plots = []

        plots.append(Plot.make1D("MET",
            tree.MET.sumet, noSel,
            EqBin(100, 0., 2000.), title="MET (GeV)"))

        return plots
