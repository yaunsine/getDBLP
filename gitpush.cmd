set commitMsg=%1
if "%commitMsg%" == "" (
    set commitMsg = "update"
)
git add .
git commit -m "%commitMsg%"
git push origin master