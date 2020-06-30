@echo off

pushd %~dp0..

echo .
mypy ".\\"

popd
