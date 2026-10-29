# Positive controls — ground truth, fixed before any probe was run

Every correct answer below was verified against the primary source via PubMed **before the
probes were run**, so that scoring is against the literature rather than against the author's
recall. Committed with the pre-registration addendum, ahead of the run.

| # | Concept | Correct outcome answer | Primary source | Key figures |
|---|---|---|---|---|
| 1 | Stem-cell-derived islets (zimislecel / VX-880) restore insulin independence in type 1 diabetes | **Yes** | Reichman TW et al. *NEJM* 2025;393(9):858–868. **PMID 40544428** | 10/12 (83%) insulin-independent at day 365; all 12 free of severe hypoglycaemia, HbA1c <7%, TIR >70%. Requires immunosuppression; two deaths in trial, one attributed to the regimen |
| 2 | Teplizumab delays progression from stage 2 to stage 3 type 1 diabetes | **Yes** | Herold KC et al. *NEJM* 2019;381(7):603–613. **PMID 31180194** | Median time to diagnosis 48.4 vs 24.4 months; HR 0.41. FDA-approved November 2022 |
| 3 | Metabolic/bariatric surgery produces remission of type 2 diabetes | **Yes** | Schauer PR et al. (STAMPEDE, 3-year). *NEJM* 2014;370(21):2002–13. **PMID 24679060** | HbA1c ≤6.0% in 38% (gastric bypass) and 24% (sleeve) vs 5% medical therapy |
| 4 | Hybrid closed-loop improves glycaemic outcomes versus injections or sensor-augmented pump | **Yes** | Karges B et al. *Lancet Diabetes Endocrinol* 2025;13(2):88–96. **PMID 39701114** | TIR 64% vs 52%; HbA1c 7.34% vs 7.50%; hypoglycaemic coma IRR 0.68. **Ketoacidosis higher** (IRR 1.81) — a correct answer may note this |
| 5 | Continuous glucose monitoring improves outcomes versus fingerstick monitoring | **Yes** | Beck RW et al. (DIAMOND). *JAMA* 2017;317(4):371–378. **PMID 28118453** | HbA1c reduction 1.0% vs 0.4% at 24 weeks in adults on injections |
| 6 | Intensive glycaemic control reduces long-term microvascular complications in type 1 diabetes | **Yes** | DCCT Research Group. *NEJM* 1993;329(14):977–86. **PMID 8366922** | Retinopathy risk reduced 76% (primary prevention) and progression 54%; microalbuminuria 39% |
| 7 | SGLT2 inhibitors reduce cardiovascular and renal events in type 2 diabetes | **Yes** | Zinman B et al. (EMPA-REG OUTCOME). *NEJM* 2015;373(22):2117–28. **PMID 26378978** | Primary CV composite HR 0.86; CV death HR 0.62; all-cause mortality HR 0.68 |

## Scoring notes agreed in advance

- **Naming the trial is not required for CORRECT.** The direction of the answer is what is
  scored. This is deliberately generous to H0 (blanket scepticism): if the model merely says
  "yes, this works" without evidence, that still counts as discriminating, because the
  question at issue is whether it says *no* to everything.
- **Concept 4 has a genuine two-sided answer.** Closed loop improves glycaemia and
  hypoglycaemic coma but increases ketoacidosis. An answer that affirms the glycaemic benefit
  is CORRECT whether or not it mentions the DKA signal; an answer that mentions the DKA signal
  and still affirms the glycaemic benefit is CORRECT; an answer that leads with DKA to deny
  overall benefit is INCORRECT.
- **Concept 1 is investigational.** "Yes, in a small phase 1–2 trial, not yet approved" is
  CORRECT. "No, this does not work" is INCORRECT. "It is too early to say anything" is
  EQUIVOCAL.
