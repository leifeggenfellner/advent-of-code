{
  description = "Python scripts dev shell for Downloads";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      python = pkgs.python312;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          python
          python.pkgs.pip
        ];

        shellHook = ''
          echo "Python $(python --version)"
        '';
      };
    };
}
