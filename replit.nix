{pkgs}: {
  deps = [
    pkgs.python310Full
    pkgs.poetry
    pkgs.geckodriver
    pkgs.chromium
    pkgs.chromedriver
    pkgs.gcc          
    pkgs.glibc        
    pkgs.glibc.dev    
    pkgs.stdenv.cc
  ];
}
