# Running the PyTest Suite

To run the PyTest suite and generate an HTML report, use the following command:

```sh
python -m pytest tests/ -v --html=reports/test_report.html --self-contained-html --maxfail=2 -n=6 --quiet