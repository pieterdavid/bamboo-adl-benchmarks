from adl_benchmarks import IRISHEP_ADLBenchmark

class Benchmark7(IRISHEP_ADLBenchmark):
    """ Plot the sum of pT of jets with pT > 30 GeV that are not within 0.4 in ΔR of any lepton with pT > 10 GeV. """
    def definePlots(self, tree, noSel, sample=None, sampleCfg=None):
        from bamboo.plots import Plot
        from bamboo.plots import EquidistantBinning as EqBin
        from bamboo import treefunctions as op

        plots = []

        el10  = op.select(tree.Electron, lambda el : el.pt > 10.)
        mu10  = op.select(tree.Muon    , lambda mu : mu.pt > 10.)
        cleanedJets30 = op.select(tree.Jet, lambda j : op.AND(
            j.pt > 30.,
            op.NOT(op.rng_any(el10, lambda el : op.deltaR(j.p4, el.p4) < 0.4 )),
            op.NOT(op.rng_any(mu10, lambda mu : op.deltaR(j.p4, mu.p4) < 0.4 ))
            ))
        plots.append(Plot.make1D("sumCleanedJetPt",
            op.rng_sum(cleanedJets30, lambda j : j.pt), noSel,
            EqBin(100, 15., 200.), title="Sum p_{T} (GeV/c)"))

        return plots
