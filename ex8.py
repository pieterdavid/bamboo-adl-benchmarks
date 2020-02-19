from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark8(IRISHEP_ADLBenchmark):
    """ For events with at least three leptons and a same-flavor opposite-sign lepton pair, find the same-flavor opposite-sign lepton pair with the mass closest to 91.2 GeV and plot the transverse mass of the missing energy and the leading other lepton. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        # The plot is made for each of the different flavour categories (l+/- l-/+ l') and then summed,
        # because concatenation of containers is not (yet) supported.
        lepColl = { "El" : tree.Electron, "Mu" : tree.Muon }
        mt3lPlots = []
        for dlNm,dlCol in lepColl.items():
            dilep = op.combine(dlCol, N=2, pred=(lambda l1,l2 : op.AND(l1.charge != l2.charge)))
            hasDiLep = noSel.refine("hasDilep{0}{0}".format(dlNm), cut=(op.rng_len(dilep) > 0))
            dilepZ = op.rng_min_element_by(dilep, fun=lambda ll : op.abs(op.invariant_mass(ll[0].p4, ll[1].p4)-91.2))
            for tlNm,tlCol in lepColl.items():
                if tlCol == dlCol:
                    hasTriLep = hasDiLep.refine("hasTrilep{0}{0}{1}".format(dlNm,tlNm),
                        cut=(op.rng_len(tlCol) > 2))
                    residLep = op.select(tlCol, lambda l : op.AND(l.idx != dilepZ[0].idx, l.idx != dilepZ[1].idx))
                    l3 = op.rng_max_element_by(residLep, lambda l : l.pt)
                else:
                    hasTriLep = hasDiLep.refine("hasTriLep{0}{0}{1}".format(dlNm,tlNm),
                        cut=(op.rng_len(tlCol) > 0))
                    l3 = op.rng_max_element_by(tlCol, lambda l : l.pt)
                mtPlot = Plot.make1D("3lMT_{0}{0}{1}".format(dlNm,tlNm),
                    op.sqrt(2*l3.pt*tree.MET.pt*(1-op.cos(l3.phi-tree.MET.phi))), hasTriLep,
                    EqBin(100, 0., 250.), title="M_{T} (GeV/c^2)")
                mt3lPlots.append(mtPlot)
                plots.append(mtPlot)
        plots.append(SummedPlot("3lMT", mt3lPlots))

        return plots
