from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark6(IRISHEP_ADLBenchmark):
    """ Plot pT of the trijet system with the mass closest to 172.5 GeV in each event and plot the maximum b-tagging discriminant value among the jets in the triplet. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        plots.append(Plot.make1D("njets",
            op.rng_len(tree.Jet), noSel,
            EqBin(20, 0., 20.), title="Number of jets"))
        trijets = op.combine(tree.Jet, N=3)
        plots.append(Plot.make1D("ntrijets",
            op.rng_len(trijets), noSel,
            EqBin(100, 0., 1000.), title="Number of 3-jet combinations"))
        hadTop = op.rng_min_element_by(trijets,
            fun=lambda comb: op.abs((comb[0].p4+comb[1].p4+comb[2].p4).M()-172.5))
        hasTriJet = noSel.refine("hasTriJet", cut=(op.rng_len(trijets) > 0))
        plots.append(Plot.make1D("trijet_mass",
            (hadTop[0].p4+hadTop[1].p4+hadTop[2].p4).M(), hasTriJet,
            EqBin(100, 0., 250.), title="Trijet mass (GeV/c^{2})"))
        plots.append(Plot.make1D("trijet_topPt",
            (hadTop[0].p4+hadTop[1].p4+hadTop[2].p4).Pt(), hasTriJet,
            EqBin(100, 0., 250.), title="Trijet p_{T} (GeV/c)"))
        plots.append(Plot.make1D("trijet_maxbtag",
            op.max(op.max(hadTop[0].btag, hadTop[1].btag), hadTop[2].btag), hasTriJet,
            EqBin(100, 0., 1.), title="Trijet maximum b-tag"))

        return plots
