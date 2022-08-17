IF EXIST dist (RD /S /Q dist)
call "venv\Scripts\activate.bat"
call python py2exe_package.py py2exe
md dist\log
md dist\config
md dist\images
xcopy /y /r /s images dist\images
rmdir bulid /s /q