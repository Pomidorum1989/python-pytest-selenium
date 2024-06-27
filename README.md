# Run the pyTests
sh '''
python -m pytest tests/ -v --html=reports/test_report.html --self-contained-html --maxfail=2
'''