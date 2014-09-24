import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import urllib2
import json

schema = avro.schema.parse(open("user.avsc").read())
writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)
writer.append(
{
    "_id": "176",
    "_timestamp": "2014-08-17T00:00:00",
    "accession": {
        "genomic": [
            "ABBA01053001",
            "ABBA01053002",
            "AC103982",
            "AC_000147",
            "AMYH02031012",
            "CH471101",
            "CS025622",
            "L29488",
            "NC_000015",
            "NC_018926",
            "NG_012794",
            "NT_010194",
            "NW_001838222",
            "NW_004929399",
            "S74659"
        ],
        "rna": [
            "AK290723",
            "BC036445",
            "BC150624",
            "BQ182050",
            "BQ446640",
            "DA596050",
            "J05062",
            "L12234",
            "M55172",
            "NM_001135",
            "NM_013227",
            "U13192",
            "X17406",
            "X80278",
            "XM_006720419"
        ],
        "protein": [
            "AAA35726",
            "AAA62824",
            "AAB48068",
            "AAC60643",
            "AAH36445",
            "AAI50625",
            "BAF83412",
            "CAA35463",
            "CAI61688",
            "EAX02017",
            "EAX02018",
            "EAX02019",
            "EAX02020",
            "EAX02021",
            "NP_001126",
            "NP_037359",
            "P16112",
            "XP_006720482"
        ]
    },
    "alias": [
        "AGC1",
        "AGCAN",
        "CSPG1",
        "CSPGCP",
        "MSK16",
        "SEDK"
    ],
    "ensembl": {
        "protein": [
            "ENSP00000341615",
            "ENSP00000387356",
            "ENSP00000452682",
            "ENSP00000453003",
            "ENSP00000453342",
            "ENSP00000453499",
            "ENSP00000453581",
            "ENSP00000484456"
        ],
        "gene": "ENSG00000157766",
        "transcript": [
            "ENST00000352105",
            "ENST00000439576",
            "ENST00000558207",
            "ENST00000558604",
            "ENST00000558704",
            "ENST00000559004",
            "ENST00000560601",
            "ENST00000561243",
            "ENST00000617301"
        ]
    },
    "entrezgene": 176,
    "exons": {
        "NM_001135": {
            "chr": "15",
            "strand": 1,
            "exons": [
                [
                    89346673,
                    89347040
                ],
                [
                    89379430,
                    89379507
                ],
                [
                    89381893,
                    89382277
                ],
                [
                    89383242,
                    89383417
                ],
                [
                    89384970,
                    89385098
                ],
                [
                    89386585,
                    89386879
                ],
                [
                    89388735,
                    89389113
                ],
                [
                    89390473,
                    89390648
                ],
                [
                    89391141,
                    89391269
                ],
                [
                    89392668,
                    89392962
                ],
                [
                    89395024,
                    89395264
                ],
                [
                    89398082,
                    89402648
                ],
                [
                    89414612,
                    89414771
                ],
                [
                    89415233,
                    89415316
                ],
                [
                    89416111,
                    89416256
                ],
                [
                    89417635,
                    89418585
                ]
            ],
            "txstart": 89346673,
            "cdsstart": 89379437,
            "cdsend": 89417712,
            "txend": 89418585
        },
        "NM_013227": {
            "chr": "15",
            "strand": 1,
            "exons": [
                [
                    89346673,
                    89347040
                ],
                [
                    89379430,
                    89379507
                ],
                [
                    89381893,
                    89382277
                ],
                [
                    89383242,
                    89383417
                ],
                [
                    89384970,
                    89385098
                ],
                [
                    89386585,
                    89386879
                ],
                [
                    89388735,
                    89389113
                ],
                [
                    89390473,
                    89390648
                ],
                [
                    89391141,
                    89391269
                ],
                [
                    89392668,
                    89392962
                ],
                [
                    89395024,
                    89395264
                ],
                [
                    89398082,
                    89402648
                ],
                [
                    89403556,
                    89403670
                ],
                [
                    89414612,
                    89414771
                ],
                [
                    89415233,
                    89415316
                ],
                [
                    89416111,
                    89416256
                ],
                [
                    89417072,
                    89417255
                ],
                [
                    89417635,
                    89418585
                ]
            ],
            "txstart": 89346673,
            "cdsstart": 89379437,
            "cdsend": 89417712,
            "txend": 89418585
        }
    },
    "generif": [
        {
            "text": "no correlation between the number of tandem repeats and scoliosis severity",
            "pubmed": "11898616"
        },
        {
            "text": "Cleavage of the carboxyl tail from the G3 domain of aggrecan but not versican and identification of the amino acids involved in the degradation",
            "pubmed": "11932252"
        },
        {
            "text": "cleaved by ADAMTS1 and diffrenteially inhibited by metalloproteinase inhibitors",
            "pubmed": "12054629"
        },
        {
            "text": "Peptide p135H, corresponding to the peptide sequence in the G3 domain of human cartilage proteoglycan aggrecan, is immunogenic/arthritogenic in BALB/c mice",
            "pubmed": "14558103"
        },
        {
            "text": "The amount of aggrecan may be related to motor aspects of intermittent exotropia",
            "pubmed": "14627072"
        },
        {
            "text": "alternative splicing in the aggrecan G3 domain may be a mechanism for modulating interactions and extracellular matrix assembly",
            "pubmed": "14722076"
        },
        {
            "text": "the interaction between aggrecan and hyaluronan in cartilage is stabilized by Link protein",
            "pubmed": "14724283"
        },
        {
            "text": "peptide fingerprinting showed that cartilage link protein and AG1 interact in the absence or presence of hyaluronan",
            "pubmed": "15590670"
        },
        {
            "text": "Data demonstrate a significant reduction of collagens I, II and aggrecan mRNA after the initiation of culture compared with mRNA levels in fresh tissue.",
            "pubmed": "16001263"
        },
        {
            "text": "A mutation in the variable repeat region of the aggrecan gene (AGC1) causes a form of spondyloepiphyseal dysplasia associated with severe, premature osteoarthritis.",
            "pubmed": "16080123"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "16402214"
        },
        {
            "text": "variable number of tandem repeat polymorphism of the aggrecan gene in 227 HTLV-I associated myelopathy/tropical spastic paraparesis patients, in 217 HTLV-I-infected healthy carriers, and in 85 normal controls",
            "pubmed": "16402214"
        },
        {
            "text": "relationship between aggrecan structure and function; role of polymorphism in intervertebral disc and articular cartilage degeneratin [review]",
            "pubmed": "16425147"
        },
        {
            "text": "establishing directly the relative residence time of these molecules in human intervertebral disc matrix",
            "pubmed": "16537531"
        },
        {
            "text": "the cleavage of aggregable aggrecan occurred in concrete peptide bonds within the CS-1 and CS-2 attachment domains",
            "pubmed": "16574327"
        },
        {
            "text": "This study demonstrates that elevated aggrecan expression and its secretion are aberrant features of Hutchinson-Gilford Progeria Syndrome.",
            "pubmed": "16650460"
        },
        {
            "text": "Despite the negative association reported here, further investigation of the gene and its potential association to familial idiopathic scoliosis is required.",
            "pubmed": "16741449"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "16741449"
        },
        {
            "text": "Results show an aggrecan product with the COOH terminal neoepitope VPGVA is synthesized by intracellular processing in chondrocytes; M-calpain is the major candidate of the proteinase to generate this product during intracellular aggrecan processing.",
            "pubmed": "17261541"
        },
        {
            "text": "Human cells cultured over 5 days increased expression of aggrecan and collagen II in both nucleus and annulus cells under increasing osmolarity.",
            "pubmed": "17568421"
        },
        {
            "text": "COMP/TSP5 may function to support matrix interactions with aggrecan in cartilage extracellular matrix",
            "pubmed": "17588949"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "17632389"
        },
        {
            "text": "The findings provide additional support for the role of the aggrecan gene VNTR polymorphism in intervertebral disc degeneration.",
            "pubmed": "17632389"
        },
        {
            "text": "mRNAs for type II collagen and aggrecan were expressed by MSCs treated with either TGFbeta1 or OP-1; however, substantial matrix production was not induced.",
            "pubmed": "18040638"
        },
        {
            "text": "we conclude from the region-specific patterns that the aggrecan-based extracellular matrix is adapted to the fast processing of sensorimotor activities",
            "pubmed": "18055126"
        },
        {
            "text": "Observational study and genome-wide association study of gene-disease association. (HuGE Navigator)",
            "pubmed": "18391952"
        },
        {
            "text": "The number of aggrecan-based perineural nets in the parietal cortex of transgenic mice is not significantly reduced when compared to the wild-type. There is a loss of hyaluronan and aggrecan components in the amyloid plaque core and coronal zone.",
            "pubmed": "18829133"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "19004047"
        },
        {
            "text": "there was an association between the aggrecan gene variable number of tandem repeats polymorphism and rheumatoid arthritis",
            "pubmed": "19004047"
        },
        {
            "text": "This protein has been found differentially expressed in the temporal lobe from patients with schizophrenia.",
            "pubmed": "19034380"
        },
        {
            "text": "There is a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and, thereby, height.",
            "pubmed": "19110214"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "19180518"
        },
        {
            "text": "in the human cerebral cortex, discrete, layer-specific PNNs are assembled through the participation of selected aggrecan isoforms that characterize defined subsets of cortical neurons",
            "pubmed": "19220578"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "19266077"
        },
        {
            "text": "Aggrecan was deposited in the myxoid and chondroid stroma of salivary pleomorphic adenomas.",
            "pubmed": "19294492"
        },
        {
            "text": "Results indicate that CCN2/CTGF binds to aggrecan through its N-terminal IGFBP and VWC modules, and this binding may be related to the CCN2/CTGF-enhanced production and secretion of aggrecan by chondrocytes.",
            "pubmed": "19298220"
        },
        {
            "text": "Application of both mechanical loads resulted in significant alterations of gene expression of PTN (+67%, P = 0.004 in anulus cells; +29%, P = 0.03 in nucleus cells) and aggrecan (+42%, P = 0.03 in anulus cells, -25%, P = 0.03 in nucleus cells).",
            "pubmed": "19333097"
        },
        {
            "text": "Levels of aggrecan ARGS fragments in human synovial fluid are increased in arthritis, osteoarthritis and following knee injury.",
            "pubmed": "19545413"
        },
        {
            "text": "A novel HtrA1-susceptible cleavage site within the interglobular domain (IGD) of aggrecan was identified.",
            "pubmed": "19657146"
        },
        {
            "text": "The aggrecan was prominently immunolocalised in the cartilaginous vertebral body rudiments and to a lesser extent within the foetal intervertebral disc.",
            "pubmed": "19669783"
        },
        {
            "text": "Hypoxia not only induces type II collagen and aggrecan, but it also inhibits type I and type III collagen in the hypoxia-inducible factor 1alpha-dependent redifferentiation of chondrocytes.",
            "pubmed": "19790048"
        },
        {
            "text": "Observational study and genome-wide association study of gene-disease association. (HuGE Navigator)",
            "pubmed": "19893584"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "19913121"
        },
        {
            "text": "A genome-wide linkage analysis identified aggrecan (ACAN) as a prime candidate gene for the osteochondritis dissecans.",
            "pubmed": "20137779"
        },
        {
            "text": "An underlying additive and multiplicative interaction is observed between the aggrecan gene VNTR polymorphism and smoking in symptomatic disc degeneration of Chinese Han in northern China.",
            "pubmed": "20367118"
        },
        {
            "text": "Observational study of gene-disease association and gene-environment interaction. (HuGE Navigator)",
            "pubmed": "20367118"
        },
        {
            "text": "This study revealed that the polymorphisms of the VDR and aggrecan genes are associated with disc degeneration and herniation.",
            "pubmed": "20367178"
        },
        {
            "text": "Clinical trial of gene-disease association and gene-environment interaction. (HuGE Navigator)",
            "pubmed": "20379614"
        },
        {
            "text": "Carrying shorter AGC1 alleles with less than 24 repeats could predispose a subject to lumbar disk degeneration disease in northern Iran.",
            "pubmed": "20496110"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "20496110"
        },
        {
            "text": "Data show an association between the distribution of aggrecan gene VNTR polymorphism and the expression of aggrecan in symptomatic LDH.",
            "pubmed": "20505571"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "20505571"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "20546612"
        },
        {
            "text": "Data indicate that calpains are involved in the C-terminal truncation of aggrecan and might have a minor role in arthritic diseases.",
            "pubmed": "20618160"
        },
        {
            "text": "Observational study of gene-disease association, gene-environment interaction, and pharmacogenomic / toxicogenomic. (HuGE Navigator)",
            "pubmed": "20628086"
        },
        {
            "text": "analysis of interleukin-6, vascular endothelial growth factor, YKL-40, matrix metalloproteinase-3, and total aggrecan in spondyloarthritis patients during 3 years of treatment with TNFalpha inhibitors",
            "pubmed": "20640910"
        },
        {
            "text": "The sstructure of an unglycosylated 30 kDa peptide from the chondroitin sulphate (CS)-attachment region of human aggrecan (CS-peptide), which was predicted to be intrinsically disordered was compared with the adjacent aggrecan G3 domain.",
            "pubmed": "20806220"
        },
        {
            "text": "Carrying a copy of the aggrecan allele with 21 repeats may increase the risk of multiple disc degeneration in subjects less than 40 years of age.",
            "pubmed": "20936487"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "20936487"
        },
        {
            "text": "Observational study of gene-disease association. (HuGE Navigator)",
            "pubmed": "21039430"
        },
        {
            "text": "Confocal immunostaining demonstrated colocalization of m-calpain and the aggrecan product within the lower hypertrophic chondrocytes and in limited region of the pericellular matrix.",
            "pubmed": "21117903"
        },
        {
            "text": "Data show that a molecular complex of fibronectin and aggrecan predicts response to lumbar ESI for radiculopathic back pain with HNP.",
            "pubmed": "21224775"
        },
        {
            "text": "The cell-specific production rate of MIA was quantitatively proportional to the aggrecan gene expression level in the early and middle phase of cartilage chondrocyte differentiation.",
            "pubmed": "21277254"
        },
        {
            "text": "This study tests the hypothesis that disease severity is characterized by alterations in expression of cartilage-specific genes for aggrecan and collagen type II.",
            "pubmed": "21655647"
        },
        {
            "text": "The objective of the present study was to assess the immunolocalization of aggrecan in the annulus, and to assess molecular gene expression patterns in the annulus extracellular matrix.",
            "pubmed": "21689646"
        },
        {
            "text": "In Turkish population, short repeated alleles of the aggrecan gene are associated with increased disc degeneration and disc herniation.",
            "pubmed": "21948754"
        },
        {
            "text": "Yiqi Huayu Bushen Recipe increased the expression of aggrecan, decreased the expression of type X collagen, and promoted cell proliferation in cells from degenerated human intervertebral discs.",
            "pubmed": "22015197"
        },
        {
            "text": "Increased expression of collagen II, aggrecan, and cartilage oligomeric matrix protein (COMP), were observed during differentiation of induced pluripotent stem cells from osteoarthritic chondrocytes.",
            "pubmed": "22241609"
        },
        {
            "text": "In the CNS, aggrecan is expressed in a precise and tightly regulated manner both temporally and spatially. (Review)",
            "pubmed": "22297263"
        },
        {
            "text": "The concentration of aggrecan, biglycan, and decorin was determined in six regions of the human supraspinatus tendon.",
            "pubmed": "22329809"
        },
        {
            "text": "The reduction in keratan sulfate levels and the strong correlation between chondroitin 6-sulfate and keratan sulfate levels indi-cates suppressed cartilage turnover after arthroscopic surgery.",
            "pubmed": "22441960"
        },
        {
            "text": "Data suggest that matrix metalloproteinases are mainly involved in normal aggrecan turnover in extracellular matrix and may have less-active roles in aggrecan degradation during knee injury or osteoarthritis (where aggrecanase-1 has central role).",
            "pubmed": "22670872"
        },
        {
            "text": "Identification of enhancer sequences involved in the regulation of expression of the human ACAN gene.",
            "pubmed": "22820679"
        },
        {
            "text": "aggrecan alleles with shorter VNTR length have a role in intervertebral disc degeneration, while VDR (TaqI, FokI, ApaI) gene polymorphisms do not [meta-analysis]",
            "pubmed": "23209686"
        },
        {
            "text": "The total mole fraction of unelongated xylose residues per aggrecan was significantly less (p = 0.03) after IL-1beta treatment compared to control cultures.",
            "pubmed": "23237500"
        },
        {
            "text": "Data indicate link protein peptide (LPP) upregulates expression of aggrecan and collagen II at both mRNA and protein levels.",
            "pubmed": "23370687"
        },
        {
            "text": "ADAMTS-4_v1 is expressed as a protein in vivo in human osteoarthritis synovium, functions as an aggrecanase, and cleaves other proteoglycan substrates.",
            "pubmed": "23897278"
        },
        {
            "text": "the subsequent presentation of aggregan from ECM leads to CD4(+) T-cell activation and effector cell formation.",
            "pubmed": "24032649"
        },
        {
            "text": "significant increased risks were found among Asians with shorter alleles of Aggrecan",
            "pubmed": "24296484"
        },
        {
            "text": "PKCepsilon activation in late passage NP cells may represent a molecular basis for aggrecan availability, as part of an PKCepsilon/ERK/CREB/AP-1-dependent transcriptional program that includes upregulation of both chondrogenic genes and microRNAs",
            "pubmed": "24312401"
        },
        {
            "text": "The expression of growth differentiation factor 5 (GDF5) and aggrecan in 15 cases of salivary gland pleomorphic adenomas, was investigated.",
            "pubmed": "24398992"
        }
    ],
    "genomic_pos": {
        "start": 88803443,
        "chr": "15",
        "end": 88875354,
        "strand": 1
    },
    "go": {
        "CC": [
            {
                "term": "extracellular region",
                "id": "GO:0005576",
                "evidence": "TAS"
            },
            {
                "term": "proteinaceous extracellular matrix",
                "id": "GO:0005578",
                "evidence": "IEA"
            },
            {
                "term": "Golgi lumen",
                "id": "GO:0005796",
                "evidence": "TAS"
            },
            {
                "term": "extracellular matrix",
                "id": "GO:0031012",
                "qualifier": "colocalizes_with",
                "evidence": "IDA"
            },
            {
                "term": "lysosomal lumen",
                "id": "GO:0043202",
                "evidence": "TAS"
            }
        ],
        "MF": [
            {
                "term": "extracellular matrix structural constituent",
                "pubmed": 1569188,
                "id": "GO:0005201",
                "evidence": "TAS"
            },
            {
                "term": "protein binding",
                "pubmed": 17588949,
                "id": "GO:0005515",
                "evidence": "IPI"
            },
            {
                "term": "hyaluronic acid binding",
                "id": "GO:0005540",
                "evidence": "IEA"
            },
            {
                "term": "carbohydrate binding",
                "id": "GO:0030246",
                "evidence": "IEA"
            },
            {
                "term": "metal ion binding",
                "id": "GO:0046872",
                "evidence": "IEA"
            }
        ],
        "BP": [
            {
                "term": "skeletal system development",
                "pubmed": 1569188,
                "id": "GO:0001501",
                "evidence": "NAS"
            },
            {
                "term": "carbohydrate metabolic process",
                "id": "GO:0005975",
                "evidence": "TAS"
            },
            {
                "term": "proteolysis",
                "pubmed": 1569188,
                "id": "GO:0006508",
                "evidence": "NAS"
            },
            {
                "term": "cell adhesion",
                "id": "GO:0007155",
                "evidence": "IEA"
            },
            {
                "term": "keratan sulfate biosynthetic process",
                "id": "GO:0018146",
                "evidence": "TAS"
            },
            {
                "term": "extracellular matrix disassembly",
                "id": "GO:0022617",
                "evidence": "TAS"
            },
            {
                "term": "extracellular matrix organization",
                "id": "GO:0030198",
                "evidence": "TAS"
            },
            {
                "term": "glycosaminoglycan metabolic process",
                "id": "GO:0030203",
                "evidence": "TAS"
            },
            {
                "term": "keratan sulfate metabolic process",
                "id": "GO:0042339",
                "evidence": "TAS"
            },
            {
                "term": "keratan sulfate catabolic process",
                "id": "GO:0042340",
                "evidence": "TAS"
            },
            {
                "term": "small molecule metabolic process",
                "id": "GO:0044281",
                "evidence": "TAS"
            }
        ]
    },
    "HGNC": "319",
    "homologene": {
        "genes": [
            [
                9606,
                176
            ],
            [
                7955,
                497505
            ],
            [
                7955,
                559593
            ],
            [
                8364,
                100491091
            ]
        ],
        "id": 136177
    },
    "HPRD": "01123",
    "interpro": [
        {
            "short_desc": "C-type_lectin",
            "id": "IPR001304",
            "desc": "C-type lectin"
        },
        {
            "short_desc": "C-type_lectin_fold",
            "id": "IPR016187",
            "desc": "C-type lectin fold"
        },
        {
            "short_desc": "EGF-like_Ca-bd_dom",
            "id": "IPR001881",
            "desc": "EGF-like calcium-binding domain"
        },
        {
            "short_desc": "EGF_extracell",
            "id": "IPR013111",
            "desc": "EGF-like domain, extracellular"
        },
        {
            "short_desc": "EG-like_dom",
            "id": "IPR000742",
            "desc": "Epidermal growth factor-like domain"
        },
        {
            "short_desc": "Ig_V-set",
            "id": "IPR013106",
            "desc": "Immunoglobulin V-set domain"
        },
        {
            "short_desc": "Ig_V-set_subgr",
            "id": "IPR003596",
            "desc": "Immunoglobulin V-set, subgroup"
        },
        {
            "short_desc": "Ig_sub",
            "id": "IPR003599",
            "desc": "Immunoglobulin subtype"
        },
        {
            "short_desc": "Ig-like_dom",
            "id": "IPR007110",
            "desc": "Immunoglobulin-like domain"
        },
        {
            "short_desc": "Link",
            "id": "IPR000538",
            "desc": "Link"
        },
        {
            "short_desc": "Sushi_SCR_CCP",
            "id": "IPR000436",
            "desc": "Sushi/SCR/CCP"
        }
    ],
    "ipi": [
        "IPI00027377",
        "IPI00291932",
        "IPI00793748"
    ],
    "map_location": "15q26.1",
    "MIM": "155760",
    "name": "aggrecan",
    "pathway": {
        "reactome": [
            {
                "name": "Metabolism",
                "id": "REACT_111217"
            },
            {
                "name": "Disease",
                "id": "REACT_116125"
            },
            {
                "name": "Degradation of the extracellular matrix",
                "id": "REACT_118572"
            },
            {
                "name": "Extracellular matrix organization",
                "id": "REACT_118779"
            },
            {
                "name": "Keratan sulfate biosynthesis",
                "id": "REACT_121120"
            },
            {
                "name": "Keratan sulfate/keratin metabolism",
                "id": "REACT_121288"
            },
            {
                "name": "Glycosaminoglycan metabolism",
                "id": "REACT_121315"
            },
            {
                "name": "MPS VI - Maroteaux-Lamy syndrome",
                "id": "REACT_147719"
            },
            {
                "name": "MPS II - Hunter syndrome",
                "id": "REACT_147734"
            },
            {
                "name": "MPS IX - Natowicz syndrome",
                "id": "REACT_147739"
            },
            {
                "name": "MPS IIID - Sanfilippo syndrome D",
                "id": "REACT_147749"
            },
            {
                "name": "MPS IIIA - Sanfilippo syndrome A",
                "id": "REACT_147753"
            },
            {
                "name": "MPS VII - Sly syndrome",
                "id": "REACT_147759"
            },
            {
                "name": "MPS IIIB - Sanfilippo syndrome B",
                "id": "REACT_147788"
            },
            {
                "name": "MPS IV - Morquio syndrome B",
                "id": "REACT_147798"
            },
            {
                "name": "MPS IV - Morquio syndrome A",
                "id": "REACT_147825"
            },
            {
                "name": "Mucopolysaccharidoses",
                "id": "REACT_147853"
            },
            {
                "name": "MPS I - Hurler syndrome",
                "id": "REACT_147857"
            },
            {
                "name": "MPS IIIC - Sanfilippo syndrome C",
                "id": "REACT_147860"
            },
            {
                "name": "ECM proteoglycans",
                "id": "REACT_163906"
            },
            {
                "name": "Metabolism of carbohydrates",
                "id": "REACT_474"
            }
        ],
        "wikipathways": [
            {
                "name": "Spinal Cord Injury",
                "id": "WP2431"
            },
            {
                "name": "Endochondral Ossification",
                "id": "WP474"
            }
        ]
    },
    "pharmgkb": "PA24616",
    "prosite": [
        "PS50026",
        "PS50041",
        "PS50099",
        "PS50315",
        "PS50835",
        "PS50923",
        "PS50963"
    ],
    "reagent": {
        "NOVART_hs-genome_siRNA": [
            {
                "id": "GNF097549",
                "relationship": "is"
            },
            {
                "id": "GNF098006",
                "relationship": "is"
            },
            {
                "id": "GNF137204",
                "relationship": "is"
            },
            {
                "id": "GNF137661",
                "relationship": "is"
            }
        ],
        "GNF_Qia_hs-genome_v1_siRNA": [
            {
                "id": "GNF176525",
                "relationship": "is"
            },
            {
                "id": "GNF187431",
                "relationship": "is"
            },
            {
                "id": "GNF198337",
                "relationship": "similar to"
            },
            {
                "id": "GNF209243",
                "relationship": "is"
            }
        ]
    },
    "refseq": {
        "genomic": [
            "AC_000147",
            "NC_000015",
            "NC_018926",
            "NG_012794",
            "NT_010194",
            "NW_001838222",
            "NW_004929399"
        ],
        "rna": [
            "NM_001135",
            "NM_013227",
            "XM_006720419"
        ],
        "protein": [
            "NP_001126",
            "NP_037359",
            "XP_006720482"
        ]
    },
    "reporter": {
        "HG-U133_Plus_2": [
            "1554950_at",
            "205679_x_at",
            "207692_s_at",
            "217161_x_at"
        ],
        "HG-U95Av2": [
            "38965_at",
            "39206_s_at",
            "39207_r_at"
        ]
    },
    "retired": 404712,
    "summary": "This gene is a member of the aggrecan/versican proteoglycan family. The encoded protein is an integral part of the extracellular matrix in cartilagenous tissue and it withstands compression in cartilage. Mutations in this gene may be involved in skeletal dysplasia and spinal degeneration. Multiple alternatively spliced transcript variants that encode different protein isoforms have been observed in this gene. [provided by RefSeq, Jul 2008].",
    "symbol": "ACAN",
    "taxid": 9606,
    "type_of_gene": "protein-coding",
    "unigene": [
        "Hs.2159",
        "Hs.616395"
    ],
    "uniprot": {
        "TrEMBL": [
            "E7ENV9",
            "E7EX88",
            "H0YK70",
            "H0YM81",
            "H0YMF1",
            "Q6PID9"
        ]
    },
    "Vega": "OTTHUMG00000171989"
}
)

writer.close()

reader = DataFileReader(open("users.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()

