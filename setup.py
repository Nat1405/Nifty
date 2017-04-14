from distutils.core import setup
setup(name='nifty',
              version='0.1.0',
                    py_modules=['src.nifsDefs','src.nifsFluxCalib','src.nifsMerge','src.nifsReduce','src.nifsScience','src.nifsSort','src.nifsTelluric'],
                    scripts=['src/nifty'],
                    data_files=[('', ['src/vega_ext.fits']),
                                ('', ['src/starstemp.txt'])
                                ('', ['src/README.md']),
                                ('', ['src/LICENSE']),
                                ('', ['src/nifs_pipeline_june_2015.pdf'])],
                          )
