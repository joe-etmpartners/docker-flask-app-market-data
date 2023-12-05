# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:42:53 2022

@author: josep
"""

yahoo_index_symbols = ['^GSPC','^DJI','^IXIC','^RUT','^AORD','^FTSE',
                       '^N225','^VIX']

yahoo_commodities_symbols = ['CL=F','RB=F','HO=F','NG=F',
                             'GC=F','SI=F','ALI=F','PL=F','HG=F',
                             'ZW=F','ZC=F']

yahoo_interest_rate_symbols = ['^TYX','^TNX','^FVX','^IRX']

yahoo_currency_pairs = ['EUR=X','GBP=X','JPY=X','CAD=X','AUD=X',
                        'NZD=X','SGD=X','TWD=X','INR=X','RUB=X','CNY=X',
                        'TRY=X','BRL=X','MXN=X']

yahoo_symbol_lists = {'index_symbols':yahoo_index_symbols,
                      'commodity_symbols':yahoo_commodities_symbols,
                      'interest_rate_symbols':yahoo_interest_rate_symbols,
                      'currency_pairs':yahoo_currency_pairs}


sector_etfs = ['XRT','XPH','XME','KIE','XHB''XHS','XHE','KCE',
               'XBI','XSD','XSW','XTN', 'XLP','XLY','XLC','XLF',
               'XLV','XLI','XLB','XLRE','XLK','XLU','XLE']

xle_components = ['XOM','CVX','SLB','COP','EOG','MPC','PXD',
                  'VLO','PSX','OXY','WMB','DVN','HES','KMI',
                  'HAL','OKE','BKR','FANG','CTRA','MRO',
                  'TRGP','APA','EQT']

xlu_components = ['NEE','DUK','SO','D','SRE','AEP','EXC',
                  'XEL','ED','PEG','WEC','ES','CEG','AWK',
                  'PCG','EIX','ETR','AEE','DTE','FE','PPL',
                  'CNP','AES','CMS','ATO','EVRG','LNT','NI',
                  'PNW','NRG']

xlk_components = ['AAPL','MSFT','NVDA','V','MA','AVGO','CSCO',
                  'ACN','ADBE','TXN','CRM','IBM','ORCL','QCOM',
                  'INTU','INTC','AMD','ADP','ADI','AMAT','PYPL',
                  'NOW','FISV','LRCX','MU','KLAC','SNPS','ROP',
                  'APH','CDNS','MSI','ADSK','FIS','NXPI','MCHP',
                  'ENPH','PAYX','TEL','FTNT','KEYS','ANET','CTSH',
                  'ON','IT','GPN','GLW','CDW','HPQ','ANSS','HPE',
                  'VRSN','TDY','EPAM','SEDG','BR','MPWR','FSLR',
                  'PAYC','SWKS','FLT','TYL','TER','AKAM',
                  'JKHY','ZBRA','NTAP','PTC','GEN','TRMB','JNPR',
                  'STX','WDC','CDAY','QRVO','FFIV','DXC']

xlre_components = ['PLD','AMT','EQIX','CCI','PSA','O','SPG',
                   'VICI','WELL','SBAC','DLR','CBRE','WY',
                   'AVB','ARE','EQR','EXR','VTR','MAA','INVH',
                   'IRM','ESS','PEAK','KIM','CPT','UDR','HST',
                   'BXP','REG','FRT','VNO']

xlb_components = ['LIN','APD','SHW','FCX','CTVA','NEM','ECL',
                  'DOW','NUE','DD','PPG','IFF','ALB','VMC',
                  'LYB','MLM','AMCR','CF','STLD','BALL','FMC',
                  'MOS','AVY','IP','PKG','CE','EMN','WRK','SEE']

xli_components = ['RTX','HON','UNP','UPS','CAT','DE','LMT',
                  'BA','GE','NOC','MMM','CSX','ETN','ITW','WM',
                  'NSC','EMR','GD','JCI','FDX','CTAS','LHX',
                  'TT','PH','CARR','PCAR','CMI','OTIS','TDG',
                  'AME','CSGP','ROK','VRSK','FAST','RSG','ODFL',
                  'CPRT','GWW','URI','EFX','FTV','IR','DAL','PWR',
                  'LUV','XYL','DOV','WAB','IEX','EXPD','J','TXT',
                  'JBHT','HWM','LDOS','NDSN','UAL','SNA','SWK',
                  'CHRW','MAS','ALLE','HII','ROL','AAL','RHI','PNR',
                  'AOS','GNRC','ALK']

xlv_components = ['UNH','JNJ','ABBV','LLY','PFE','MRK','TMO',
                  'ABT','DHR','BMY','AMGN','ELV','CVS','GILD',
                  'MDT','CI','ISRG','SYK','REGN','VRTX','BDX',
                  'ZTS','BSX','HUM','MRNA','MCK','HCA','CNC',
                  'EW','A','DXCM','BIIB','IQV','IDXX','MTD',
                  'RMD','ILMN','ABC','ZBH','BAX','CAH','LH',
                  'WAT','MOH','HOLX','STE','DGX','PKI','WST',
                  'COO','ALGN','INCY','VTRS','TECH','TFX','CRL',
                  'HSIC','UHS','BIO','CTLT','OGN','XRAY','DVA']

xlf_components = ['BRK.B','JPM','BAC','WFC','SCHW','GS','MS',
                  'SPGI','BLK','CB','AXP','C','MMC','PGR',
                  'PNC','AON','CME','USB','ICE','TFC','MET',
                  'AIG','TRV','MCO','AFL','AJG','MSCI','PRU',
                  'ALL','COF','BK','AMP','STT','WTW','DFS','MTB',
                  'TROW','HIG','ACGL','FITB','FRC','RJF','NDAQ',
                  'HBAN','RF','CFG','PFG','NTRS','CINF','KEY',
                  'WRB','FDS','SYF','BRO','CBOE','RE','SIVB',
                  'L','GL','MKTX','CMA','IVZ','BEN','ZION',
                  'SBNY','AIZ','LNC']

xlc_components = ['META','GOOGL','GOOG','DIS','TMUS','VZ','ATVI',
                  'CMCSA','T','EA','NFLX','CHTR','WBD','OMC',
                  'TTWO','IPG','MTCH','LYV','FOXA','PARA','NWSA',
                  'LUMN','FOX','DISH','NWS']

xly_components = ['AMZN','HD','TSLA','NKE','MCD','LOW','SBUX',
                  'TJX','BKNG','TGT','DG','ORLY','GM','AZO',
                  'F','ROST','MAR','CMG','YUM','HLT','DLTR',
                  'DHI','GPC','APTV','TSCO','ULTA','LEN','EBAY',
                  'DRI','BBY','LVS','ETSY','GRMN','NVR','LKQ',
                  'EXPE','DPZ','POOL','MGM','RCL','PHM','BBWI',
                  'KMX','BWA','TPR','VFC','CZR','AAP','WYNN',
                  'WHR','CCL','HAS','NCLH','MHK','NWL','RL']

xlp_components = ['PG','PEP','KO','COST','MDLZ','PM','WMT','MO',
                  'CL','EL','ADM','GIS','KMB','SYY','MNST','STZ',
                  'HSY','KHC','KDP','KR','WBA','MKC','CHD','CAG',
                  'K','TSN','CLX','SJM','HRL','LW','BF.B','CPB','TAP']

xtn_components = ['MATX','GNK','HUBG','FDX','NSC','KEX','R','AAWW',
                  'JBHT','FWRD','EGLE','UNP','UPS','CSX','GXO','LSTR',
                  'EXPD','ODFL','CHRW','DAL','SNDR','XPO','WERN',
                  'KNX','SAVE','ALK','HTZ','RXO','UHAL','AAL',
                  'SAIA','UBER','ARCB','JOBY','LYFT','ALGT',
                  'LUV','UAL','JBLU','CAR','ULCC','TSP','ATSG',
                  'SKYW','HA','MRTN','SNCY','HTLD','DSKE']

xsw_components = ['AGYS','COUP','PWSC','BOX','IMXI','PD',
                  'FOUR','CNXC','SWI','ACIW','VRNS','DOCU',
                  'PRO','TWKS','WK','FLYW','RAMP','MMS','G',
                  'MODN','BLKB','EEFT','AYX','CWAN','KD','WEX',
                  'CNDT','IDCC','ORCL','ADBE','CSGS','DXC','CRNC',
                  'ATVI','NCR','ESMT','DT','MANH','VMW','AVDX',
                  'ROP','FISV','SMAR','EVOP','SSNC','KNBE',
                  'FICO','GPN','INST','FIVN','CRM','MGI','TYL',
                  'PTC','DBX','BKI','MA','EVTC','FLT','ETWO',
                  'WU','XM','TDC','V','ENV','JKHY','EBIX','ZUO',
                  'BL','RPD','ANSS','CDNS','IT','EXLS','PRGS',
                  'INFA','SNPS','TTWO','CCCS','FORG','TTEC','IIIV',
                  'CVLT','CFLT','GDYN','ALKT','VRNT','EA','CTSH',
                  'IBM','NOW','DCT','MSFT','PRFT','YEXT','SPSC',
                  'PAYX','WDAY','PAYC','NCNO','JAMF','GWRE','ADSK',
                  'INTU','FIS','SPLK','YOU','NEWR','PAYO','ALRM',
                  'BR','RPAY','DLB','GTLB','DDOG','APPF','TENB',
                  'GEN','HUBS','PCOR','SABR','QLYS','QTWO','ADP',
                  'BRZE','FRSH','PCTY','CCSI','CDAY','FTNT','PEGA',
                  'PYPL','AZPN','ADEA','VRRM','PAYA','RELY','SQ',
                  'ESTC','PLTK','EPAM','ALTR','PATH','BILL','MITK',
                  'ACN','EGHT','BSY','ZS','RNG','PYCR','EXFY','MNTV',
                  'IOT','ZM','NABL','ATEN','SPT','CXM','ZETA','SUMO',
                  'APP','OSPN','DV','TOST','MTTR','AMPL','TASK','PANW',
                  'MQ','CRWD','BASE','ASAN','OLO','HCP','AI','S',
                  'APPS','APPN','PLTR','EVBG','RBLX','RIOT','XPER',
                  'NTNX','VERX','LPSN','AFRM','U','AVPT','HCKT','MSTR',
                  'AMSWA','DOMO','MARA','CASS','SEMR','MYPS']

xsd_components = ['AVGO','AMBA','FSLR','CRUS','RMBS','ADI','POWI',
                  'PI','MXL','SITM','TXN','SMTC','SWKS','SLAB','AMD',
                  'QCOM','ALGM','INTC','QRVO','SYNA','OLED','MU',
                  'LSCC','MCHP','NXPI','MTSI','MPWR','DIOD','ON',
                  'MRVL','WOLF','NVDA','CRDO','AOSL','INDI','SGH',
                  'NVTS','MMAT','CEVA']

xbi_components = ['MDGL','CYTK','ARWR','HZNP','AKRO','CPRX','EXAS',
                  'RYTM','ALT','PCVX','SRPT','NTRA','ACAD','RARE',
                  'BCRX','IRWD','INSM','ISEE','ALKS','MRNA','NBIX',
                  'MRTX','SGEN','ALNY','HALO','CTIC','APLS','ABBV',
                  'BMRN','IONS','RXDX','FOLD','EXEL','UTHR','KRTX',
                  'PRTA','INCY','GILD','BIIB','VIR','REGN','AMGN',
                  'DNLI','PTCT','MYOV','VRTX','SWTX','BLUE','BEAM',
                  'TWST','BPMC','NTLA','CERE','RLAY','CRSP','VCYT',
                  'DVAX','VERV','MNKD','IOVA','EDIT','TVTX','CLDX',
                  'SNDX','IMGN','SAGE','TGTX','AGIO','CDNA','KYMR',
                  'RVMD','RCKT','RNA','GOSS','KRYS','INBX','EBS',
                  'BHVN','KDNY','QURE','BBIO','CDMO','FATE','NVAX',
                  'ARQT','ALLO','ZNTL','VCEL','AGEN','DAWN','IMVT',
                  'FGEN','RCUS','DCPH','AVXL','ENTA','RXRX','KURA',
                  'INO','COGT','VRDN','ACLX','MYGN','SRNE','RGNX'
                  'ICPT','PTGX','XNCR','KROS','ADMA','MORF','OCGN',
                  'CHRS','EQRX','GERN','MIRM','IDYA','ARCT','RAPT',
                  'ALLK','MRSN','IBRX','KZR','DSGN','PMVP','ANAB',
                  'PNT','REPL','SGMO','ITOS','ROIV','ALEC','CRNX',
                  'KPTI','EGRX','SANA','NRIX','LYEL','MCRB','ATRA',
                  'ACET','KNSA','NUVL','CRBU','TSVT','ERAS','FDMT',
                  'VNDA','CCCC','ANIK','STRO','MDXG']

kce_components = ['SCHW','EVR','AMG','CBOE','CG','BEN','FOCS',
                  'MKTX','IVZ','NTRS','COWN','BK','TW','BLK',
                  'ICE','VRTS','LAZ','FHI','PIPR','ARES','LPLA',
                  'JEF','STT','IBKR','KKR','PJT','CME','JHG','SF',
                  'NDAQ','MCO','VIRT','MS','OWL','GS','AMP','SPGI',
                  'BX','SEIC','HLI','RJF','MSCI','HLNE','MC','TROW',
                  'MORN','APAM','FDS','TPG','COIN','HOOD','CNS','LPRO',
                  'DFIN','SNEX','RILY','BCOR','VCTR','STEP','BGCP',
                  'WT','BSIG','PWP','DHIL','PX','AMK','BRDG']

xhe_components = ['INSP','ALGN','COO','VIVO','XRAY','MASI','BDX',
                  'GMED','HOLX','ZBH','PEN','ICUI','ABT','TFX',
                  'ATEC','IART','NVST','BSX','TMDX','ATRC','SYK',
                  'SILK','LIVN','EW','OMCL','MDT','NEOG','ENOV',
                  'HAE','TNDM','ISRG','BAX','MMSI','PODD','IDXX',
                  'OM','NUVA','CNMD','PRCT','STE','AXNX','DXCM','RMD',
                  'ITGR','NVRO','MLAB','LNTH','NARI','NVCR','SWAV',
                  'QDEL','IRTC','FIGS','GKOS','CUTR','TMCI','HSKA',
                  'EMBC','BFLY','STAA','AVNS','UFPT','VREX','ANGO',
                  'CERS','KIDS','LMAT','OFIX','INGN','CSII','AORT',
                  'SENS','ATRI','FNA','VRAY','SIBN','AXGN','SRDX',]

xhs_components = ['UHS','THC','DGX','EHC','RCM','ENSG','SGRY','PINC',
                  'SEM','MCK','ABC','CAH','AMEH','OPCH','HCA','PRVA',
                  'CI','ACHC','LH','SGFY','ONEM','DVA','CHE','HSIC',
                  'UNH','HQY','PGNY','MOH','ELV','LHCG','PDCO','HUM',
                  'ALHC','ADUS','OSH','BKD','CNC','AMED','OMI','AGL',
                  'CVS','MD','AMN','CCRN','AHCO','FLGT','CRVL','EHAB',
                  'DCGO','CLOV','HIMS','MODV','CYH','NVTA','CANO','ME',
                  'USPH','ACCD','GH','CSTL','RDNT','LFST','OPK','AGTI',
                  'NHC','NRC']

xhb_components = ['DHI','PHM','LEN','WSM','LOW','HD','BLDR','WHR','NVR',
                  'JCI','CARR','TT','CSL','MAS','OC','LII','WMS','TOL',
                  'FND','ALLE','FBIN','MHK','AOS','TREX','BLD','TMHC',
                  'MDC','SKY','LGIH','TPH','CVCO','IBP','CCS','GRBK','MHO']

kie_components = ['RNR','ACGL','KNSL','RE','SIGI','GL','AFL','TRV',
                  'PFG','AIG','HIG','MET','CB','RGA','MKL','CINF',
                  'BHF','PRU','ORI','AFG','UNM','THG','ALL','AJG','AON',
                  'MMC','PGR','L','FAF','AGO','FNF','AXS','BRO','PRI',
                  'AEL','CNO','AIZ','RLI','LNC','TRUP',
                  'ERIE','GNW','KMPR','GSHD','ESGR','PLMR',
                  'RYAN','WTW','WRB','WTM']

xme_components = ['BTU','HL','FCX','STLD','RGLD','CMC','NEM',
                  'CEIX','ARCH','RS','NUE','ATI','AA','ARNC',
                  'PLL','CENX','CLF','CDE','UEC','EVA','CMP','KALU',
                  'CRS','TMST','MTRN','RYI','SCHN','SXC','HAYN',
                    'AMR','X','MP','WOR','FEAM']

xph_components = ['MRK','LLY','AXSM','BMY','JNJ','SAVA',
                  'PFE','ITCI','AMLX','JAZZ','RETA','RPRX','PBH',
                  'CORT','PCRX','ELAN','PRGO','AMPH','SIGA',
                  'INVA','SUPN','CTLT','RVNC','NKTR','COLL','TBPH','ACRS',
                  'ESPR','CARA','EOLS','ANIP','AVIR',
                  'PAHC','RLMD','NGM','CINC','PLRX','HRMY','ZTS',
                      'VTRS','OGN','ARVN','VTYX','NUVB']

xrt_components = ['ANF','GPS','AEO','FIVE','ODP','BURL','BKE','URBN',
                  'M','ETSY','ROST','CHWY','GES','TJX','ORLY',
                  'AZO','DDS','BBY','PAG','TSCO','GPI',
                  'SFM','SAH','EYE','ABG','ULTA','CASY',
                  'OLLI','DLTR','KSS','CHS','AN','JWN','FL','DKS','EBAY',
                  'MUSA','SIG','RVLV','HIBB','MNRO','DG','TGT','BOOT',
                  'COST','KR','GME','LAD','OSTK','HZO','CWH','BJ',
                  'IMKTA','RCII','GCO','CAL','AAP','PLCE','GO',
                  'BIG','QRTEA','SBH','PSMT','KMX','SCVL','PETS',
                  'AMZN','ACI','SFIX','RAD','DBI','CRMT',
                  'ZUMZ','SPWH','PRTS','TA','LQDT','CVNA',
                  'ONEW','VSCO','POSH','WBA','WMT','BBWI','WRBY','ASO','LESL',
                  'DASH','W','XMTR','WOOF','FRG','EVGO','WISH',
                  'WMK','WINA','ARKO']

sp500_full = ['NWL','RL','FOX','DVA','VNO','DISH','NWS',
              'GNRC','LNC','ALK','MHK', 'FRT','PNR','NWSA',
              'BEN','NCLH','AIZ','DXC', 'CTLT','RHI','HAS',
              'AOS','SEE', 'HII','AAL','AAP','FFIV','ROL','UHS','PNW',
              'IVZ','BIO','FBHS','SBNY','HSIC','NI','KMX',
              'CPB','GL','CE','TFX','EMN','VFC','CZR','TAP','JNPR',
              'PHM','STX','BWA','LYV','PARA','REG','BXP','NRG','ALLE',
              'CDAY','FOXA','QRVO','MKTX','CCL','TPR','CMA',
              'POOL','TECH','CPT','PKG','NDSN','LW','UDR','CHRW',
              'CRL','SWK','MGM','L','MAS','SNA','SIVB',
              'IPG','BRO','MTCH','EVRG','TYL','HST','IP',
              'RE','RCL','GEN','CBOE','PTC','LKQ','DPZ','PEAK','LNT',
              'JKHY','EXPE',
              'APA','COO','JBHT','TXT','LDOS','LVS','INCY','SWKS',
              'AKAM','FLT','NVR','TRMB','TER','ALGN','HRL','KIM','UAL',
              'GRMN','ESS','EQT','IRM','AVY','PAYC','ETSY',
              'SJM','OMC','FMC','SEDG','NTAP','TTWO','J','MPWR',
              'KEY','BBY','ABMD','FDS','PKI','TRGP','ATO','BR',
              'SYF','CLX','DRI','STE','CAG','MOS','IEX','DGX','CMS','CINF',
              'EPAM','TSN','CHD','CNP','NTRS',
              'TDY','MOH','AES','HOLX','EXPD','INVH','MAA','K','AMCR','VRSN',
              'LYB','RF','EQR','ACGL','CAH','PPL','CF','IR',
              'PFG','ANSS','MKC','MRO','CFG','PWR','EXR','HPE',
              'DOV','AAPL','MSFT','AMZN','GOOGL','BRK.B','GOOG',
              'UNH','TSLA','JNJ','XOM','JPM','NVDA','PG','V',
              'CVX','HD','MA','LLY','ABBV','PFE','MRK','BAC','PEP',
              'META','KO','COST','WMT','TMO','AVGO','CSCO','MCD',
              'ABT','ACN','WFC','DIS','DHR','BMY','LIN','NEE','VZ',
              'TXN','COP','CMCSA','ADBE','PM','UNH','TSLA','JNJ',
              'JPM','NVDA','PG','V','CVX',
              'HD','MA','LLY','ABBV','PFE','MRK','BAC','PEP',
              'KO','COST','TMO','AVGO','CSCO','MCD','ABT','ACN',
              'DIS','DHR','BMY','LIN','NEE',
              'TXN','COP','CMCSA','ADBE','PM',
              'AMGN,CRM,HON','RTX','T','UPS','NKE','QCOM','UNP','LOW',
              'CVS','IBM','GS','NFLX','CAT','ELV','ORCL','SCHW','DE','MS',
              'INTC','AMD','SPGI','LMT','SBUX','BLK','GILD','INTU',
              'ADP','PLD','MDT','AMT','BA','CI','TJX','GE','AXP','ISRG','C',
              'MDLZ','CB','AMAT','PYPL','TMUS','ADI','MMC','EOG',
              'MO','VRTX','NOW','BKNG','REGN','TGT','NOC','SYK','PGR','DUK',
              'SLB','SO','MMM','CSX','BDX','PNC','HUM','APD',
              'FISV','ETN','AON','CL','BSX','ITW','CME','MPC','EQIX',
              'MU','TFC','LRCX','USB','CCI','NSC','ICE','MRNA','GM','PXD',
              'DG','SHW','GD','EMR','MCK','F','ORLY','ADM','FCX','VLO','KLAC',
              'ATVI','PSX','OXY','MET','HCA','SRE','D','AZO','EL','SNPS','GIS','AEP',
              'CNC','CTVA','AIG','EW','PSA','APH','MCO','JCI','A','KMB','ROP',
              'CDNS','TRV','MAR','DVN','MSI','SYY','NXPI','DXCM','LHX','CMG',
              'CHTR','ADSK','FDX','BIIB','AJG','FIS','ENPH','MCHP','ROST',
              'AFL','STZ','EXC','TEL','IQV','PRU','MSCI','HES',
              'COF','CTAS','NUE','O','MNST','SPG','PAYX','HLT','PH',
              'KMI','CARR','DOW','NEM','ALL','PCAR','YUM','ECL',
              'AMP','DD','CMI','IDXX','HSY','ED','FTNT','EA','HAL','BK',
              'ANET','RMD','KDP','ILMN','VICI','KR',
              'WELL','AME','MTD','SBAC',
              'TDG','ALB','DLR','KEYS','KHC','PPG','CSGP','DLTR','CTSH','ON',
              'CEG','WEC','MTB','ROK','DFS','WBA','PEG','BKR','OKE','FAST','RSG',
              'ES','BAX','VRSK','GPN','APTV','CPRT','TROW','IT','STT','GWW','ODFL',
              'DHI','AWK','HPQ','WTW','ABC','FANG','IFF','GPC','GLW','CDW',
              'CBRE','HIG','FITB','TSCO','PCG','EBAY','URI','EIX','AVB',
              'VMC','ULTA','FTV','LUV','ETR',
              'EFX','ARE','NDAQ','RJF','CTRA','AEE','FRC','MLM','LEN',
              'HBAN','DAL','DTE','LH','FE',
              'ZTS','TT','WMB','XEL','OTIS','XOM','ZBH','WBD',
              'META','WMT','WY','WFC','VZ','WAT','WRB','XYL','ZBRA',
              'HWM','VTR','WAB','VTRS','BALL','WST','WDC','WRK',
              'BBWI', 'WYNN','WHR','ZION', 'XRAY', 'OGN', 'LUMN']

nasdaq100_components = ['AAPL','MSFT','GOOG','GOOGL','AMZN','NVDA',
                        'TSLA','META','PEP','AVGO','ASML','AZN',
                        'COST','CSCO','TMUS','ADBE','CMCSA','TXN',
                        'HON','AMGN','NFLX','QCOM','SBUX','PDD','INTU',
                        'INTC','GILD','AMD','ADP','ISRG','MDLZ','ADI',
                        'AMAT','JD','PYPL','BKNG','REGN','VRTX','MRNA',
                        'CSX','FISV','ATVI','LRCX','MU','MNST','ORLY',
                        'KLAC','CHTR','KDP','KHC','AEP','SNPS','NTES',
                        'MAR','CTAS','CDNS','MELI','EXC','DXCM','PANW',
                        'PAYX','ADSK','NXPI','ROST','BIIB','XEL','LULU',
                        'MCHP','FTNT','ENPH','PCAR','IDXX','EA','ABNB',
                        'WBA','WDAY','BIDU','DLTR','ODFL','MRVL','ILMN',
                        'CTSH','CEG','VRSK','FAST','SGEN','SIRI','CRWD',
                        'EBAY','VRSN','ANSS','DDOG','TEAM','ZM','ALGN',
                        'ZS','CPRT','SWKS','SPLK','MTCH','DOCU','LCID']


symbol_lists = {'sector_etfs':sector_etfs,
                'xlu_components':xlu_components,
                'xlk_components':xlk_components,
                'xlre_component':xlre_components,
                'xlb_components':xlb_components,
                'xli_components':xli_components,
                'xlv_components':xlv_components,
                'xrt_components':xrt_components,
                'xph_components':xph_components,
                'xme_components':xme_components,
                'kie_components':kie_components,
                'xhb_components':xhb_components,
                'xhs_components':xhs_components,
                'xhe_components':xhe_components,
                'kce_components':kce_components,
                'xbi_components':xbi_components,
                'xsd_components':xsd_components,
                'xsw_components':xsw_components,
                'xtn_components':xtn_components,
                'xlp_components':xlp_components,
                'xly_components':xly_components,
                'xlc_components':xlc_components,
                'xlf_components':xlf_components,
                'xle_components':xle_components,
                'sp500_components':sp500_full,
                'nasdaq100_components':nasdaq100_components
                }


