pytest -s -v -m "smoke" --html=./Report/report.html testCases/  --browser chrome
REM pytest -s -v -m "sanity" --html=./Report/report.html testCases/  --browser chrome
REM pytest -s -v -m "Regression" --html=./Report/report.html testCases/  --browser chrome