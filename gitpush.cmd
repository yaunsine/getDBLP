set files=%1
set commitMsg=%2
if "%commitMsg%" == "" (
    set commitMsg = "update"
)
git add %files%
git commit -m "%commitMsg%"
git push origin master