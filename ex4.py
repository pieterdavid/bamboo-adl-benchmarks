from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark4(IRISHEP_ADLBenchmark):
    """ Plot the missing ET of events that have at least two jets with pT > 40 GeV. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        jets40 = op.select(tree.Jet, lambda j : j.pt > 40)
        hasTwoJets40 = noSel.refine("twoJets40", cut=(op.rng_len(jets40) >= 2))
        plots.append(Plot.make1D("twoJets40_MET",
            tree.MET.sumet, hasTwoJets40,
            EqBin(100, 0., 2000.), title="MET (GeV)"))

        return plots
