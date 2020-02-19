from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark5(IRISHEP_ADLBenchmark):
    """ Plot the missing ET of events that have an opposite-sign muon pair with an invariant mass between 60 and 120 GeV. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        dimu_Z = op.combine(tree.Muon, N=2, pred=(lambda mu1, mu2 : op.AND(
            mu1.charge != mu2.charge,
            op.in_range(60., op.invariant_mass(mu1.p4, mu2.p4), 120.)
            )))
        hasDiMuZ = noSel.refine("hasDiMuZ", cut=(op.rng_len(dimu_Z) > 0))
        plots.append(Plot.make1D("dimuZ_MET",
            tree.MET.sumet, hasDiMuZ,
            EqBin(100, 0., 2000.), title="MET (GeV)"))

        return plots
