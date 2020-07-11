import pandas

pandas.read_csv("survey-results-original.csv")[[
 'PyHEP feedback: Atlantic: 15:00 CET, 06:00 PDT, 18:30 IST, 22:00 JST',
 'PyHEP feedback: Pacific: 00:00 CET, 15:00 PDT, 03:30 IST, 07:00 JST',
 'PyHEP feedback: Indian Ocean: 09:00 CET, 00:00 PDT, 12:30 IST, 16:00 JST',
 'PyHEP feedback: How did you hear about this workshop?',
 'PyHEP feedback: What are you hoping to learn from this workshop?',
 'Professional life: What best describes your occupation?',
 'Professional life: What best describes the stage of your professional career?',
 "Professional life: If you're involved in computing, what do you do?",
 'Professional life: If you write software, what is its lifespan and scope?',
 'Professional life: Are you associated with one or more experimental or theoretical collaborations? (E.g. ATLAS, CMS, DUNE, USQCD...)',
 'Computing and programming: What kind of computer do you use most often for work? (The device you physically interact with, not remote; "laptop-form" tablets with keyboards like Surface count as a laptop)',
 'Computing and programming: What operating system(s) does it run?',
 'Computing and programming: How much of your work do you do on remote computers (through ssh, web interfaces, etc.)?',
 'Computing and programming: If you work on remote computers, what kinds are they?',
 'Computing and programming: Approximately how many years ago did you write your first program (zero for never)?',
 'Computing and programming: Approximately how many years ago did you start programming regularly (zero for never)?',
 'Computing and programming: How would you describe your programming ability?',
 'Computing and programming: How did you learn to program? (Which were the most significant?)',
 'Computing and programming: Which of the following languages do you use regularly (i.e. more than 10% of your work)?',
 'Computing and programming: If you regularly use programming language(s) not listed above, please list them here',
 'Computing and programming: If you use Python, which version of Python do you primarily use right now?',
 'Computing and programming: Do you regularly use both Python 2 and 3 (more than 10% of the time each)?',
 'Computing and programming: About how often do you use Python relative to C or C++?',
 'Computing and programming: Do you *expect* to use Python more or less in the future (as a fraction of your programming time)?',
 'Computing and programming: Do you *want* to use Python more or less in the future (as a fraction of your programming time)?',
 'Computing and programming: What are your main reasons for using Python?',
 'Computing and programming: How would you characterize your main use(s) of Python?',
 'Computing and programming: What changes would increase your usage of Python?',
 'Computing and programming: Which text editors/IDEs do you use regularly (i.e. more than 10% of your work)?',
 'Computing and programming: Do you regularly use a text editor/IDE not listed here? If so, which?',
 'Computing and programming: What package manager do you regularly use to install *Python packages* (numpy, etc.)?',
 'Computing and programming: How often do you use an automated testing suite?',
 'Computing and programming: How often do you use continuous integration (CI) or continuous deployment (CD)?',
 'Computing and programming: How often do you use virtual environments (e.g. venv or conda env), virtual machines, or containers (e.g. Docker)?',
 'Computing and programming: How often do you use source control (GitHub/GitLab/BitBucket...)?',
 'Computing and programming: If you use source control, which do you most often use?',
 'Computing and programming: Is most of your code publicly available or private?',
 'Computing and programming: Do you specify a license for your code?',
 'Python ecosystem: Jupyter: https://jupyter.org',
 'Python ecosystem: IPython: https://ipython.org',
 'Python ecosystem: NumPy: https://numpy.org',
 'Python ecosystem: SciPy: https://www.scipy.org',
 'Python ecosystem: Pandas: https://pandas.pydata.org',
 'Python ecosystem: xarray: https://xarray.pydata.org',
 'Python ecosystem: Matplotlib: https://matplotlib.org',
 'Python ecosystem: Seaborn: https://seaborn.pydata.org',
 'Python ecosystem: HoloViews: https://holoviews.org',
 'Python ecosystem: Altair: https://altair-viz.github.io',
 'Python ecosystem: Bokeh: https://docs.bokeh.org',
 'Python ecosystem: Plotly: https://plotly.com',
 'Python ecosystem: Kibana: https://www.elastic.co/kibana',
 'Python ecosystem: SciKit-Learn: https://scikit-learn.org',
 'Python ecosystem: SciKit-Optimize: https://scikit-optimize.github.io',
 'Python ecosystem: SciKit-Image: https://scikit-image.org',
 'Python ecosystem: TensorFlow: https://www.tensorflow.org',
 'Python ecosystem: PyTorch: https://pytorch.org',
 'Python ecosystem: Keras: https://keras.io',
 'Python ecosystem: MXNet: https://mxnet.apache.org',
 'Python ecosystem: Theano: http://deeplearning.net/software/theano',
 'Python ecosystem: Numba: https://numba.pydata.org',
 'Python ecosystem: JAX: https://github.com/google/jax',
 'Python ecosystem: SymPy: https://www.sympy.org',
 'Python ecosystem: PySpark: https://spark.apache.org',
 'Python ecosystem: Dask: https://dask.org',
 'Python ecosystem: Vaex: https://vaex.io',
 'Python ecosystem: NetworkX: https://networkx.github.io',
 'Python ecosystem: PyMC3: https://docs.pymc.io',
 'Python ecosystem: StatsModels: https://www.statsmodels.org',
 'Python ecosystem: h5py (HDF5): https://www.h5py.org',
 "Python ecosystem: Do you regularly use any other packages that weren't listed here?",
 "Particle physics ecosystem: Your collaboration's software framework",
 "Particle physics ecosystem: Your research group's custom software tools",
 'Particle physics ecosystem: ROOT in C++: https://root.cern',
 'Particle physics ecosystem: ROOT through PyROOT: https://root.cern',
 'Particle physics ecosystem: rootpy: http://www.rootpy.org',
 'Particle physics ecosystem: Uproot: https://github.com/scikit-hep/uproot',
 'Particle physics ecosystem: Uproot 4 (new version): https://github.com/scikit-hep/uproot4',
 'Particle physics ecosystem: Awkward Array: https://github.com/scikit-hep/awkward-array',
 'Particle physics ecosystem: Awkward 1.0 (new version): https://awkward-array.org',
 'Particle physics ecosystem: root-numpy: https://scikit-hep.org/root_numpy',
 'Particle physics ecosystem: root-pandas: https://github.com/scikit-hep/root_pandas',
 'Particle physics ecosystem: mplhep: https://github.com/scikit-hep/mplhep',
 'Particle physics ecosystem: boost-histogram: https://github.com/scikit-hep/boost-histogram',
 'Particle physics ecosystem: physt: https://github.com/janpipek/physt',
 'Particle physics ecosystem: histoprint: https://github.com/scikit-hep/histoprint',
 'Particle physics ecosystem: iminuit: https://iminuit.readthedocs.io',
 'Particle physics ecosystem: zfit: https://github.com/zfit/zfit',
 'Particle physics ecosystem: LMFIT: https://lmfit.github.io/lmfit-py',
 'Particle physics ecosystem: GooFit: https://github.com/GooFit/GooFit',
 'Particle physics ecosystem: hepstats: https://github.com/scikit-hep/hepstats',
 'Particle physics ecosystem: pyhf: https://github.com/scikit-hep/pyhf',
 'Particle physics ecosystem: reana: http://reanahub.io',
 'Particle physics ecosystem: Heppy: https://github.com/cbernet/heppy',
 'Particle physics ecosystem: Coffea: https://coffeateam.github.io/coffea',
 'Particle physics ecosystem: FAST-HEP: https://github.com/FAST-HEP',
 'Particle physics ecosystem: hepunits: https://github.com/scikit-hep/hepunits',
 'Particle physics ecosystem: particle: https://github.com/scikit-hep/particle',
 'Particle physics ecosystem: pyjet: https://github.com/scikit-hep/pyjet',
 'Particle physics ecosystem: Astropy: https://www.astropy.org',
 'Particle physics ecosystem: Geant4Py: https://nusoft.fnal.gov/larsoft/doxsvn/html/md_geant4.10.03.p03_environments_g4py_README.html',
 'Particle physics ecosystem: luigi: https://luigi.readthedocs.io',
 'Particle physics ecosystem: Rucio: https://rucio.readthedocs.io',
 'Particle physics ecosystem: Gaudi: https://github.com/lgiordani/gaudi',
 'Particle physics ecosystem: Condor: https://htcondor.readthedocs.io/en/latest/apis/python-bindings',
 "Particle physics ecosystem: Do you regularly use any other packages that weren't listed here?",
]].to_csv("survey-results.csv", index=False)