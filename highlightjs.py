import re

pattern = re.compile(r'\|(.+?)\|(.+?)\|.+?\|')

# extra languages and aliases that should be supported
extras = [
    ('ANSI', ('ansi',)),
]

# https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md
languages = """| 1C                      | 1c                     |         |
| 4D                      | 4d                     |[highlightjs-4d](https://github.com/highlightjs/highlightjs-4d) |
| ABAP                    | sap-abap, abap         |[highlight-sap-abap](https://github.com/highlightjs/highlightjs-sap-abap) |
| ABNF                    | abnf                   |         |
| Access logs             | accesslog              |         |
| Ada                     | ada                    |         |
| Apex                    | apex                   | [highlightjs-apex](https://github.com/highlightjs/highlightjs-apex/)   |
| Arduino (C++ w/Arduino libs) | arduino, ino           |         |
| ARM assembler           | armasm, arm            |         |
| AVR assembler           | avrasm                 |         |
| ActionScript            | actionscript, as       |         |
| Alan IF                 | alan, i                | [highlightjs-alan](https://github.com/highlightjs/highlightjs-alan) |
| Alan                    | ln                     | [highlightjs-alan](https://github.com/alantech/highlightjs-alan) |
| AngelScript             | angelscript, asc       |         |
| Apache                  | apache, apacheconf     |         |
| AppleScript             | applescript, osascript |         |
| Arcade                  | arcade                 |         |
| AsciiDoc                | asciidoc, adoc         |         |
| AspectJ                 | aspectj                |         |
| AutoHotkey              | autohotkey             |         |
| AutoIt                  | autoit                 |         |
| Awk                     | awk, mawk, nawk, gawk  |         |
| Bash                    | bash, sh, zsh          |         |
| Basic                   | basic                  |         |
| BBCode                  | bbcode                 | [highlightjs-bbcode](https://github.com/RedGuy12/highlightjs-bbcode) |
| Blade (Laravel)         | blade                  | [highlightjs-blade](https://github.com/miken32/highlightjs-blade) |
| BNF                     | bnf                    |         |
| Brainfuck               | brainfuck, bf          |         |
| C#                      | csharp, cs             |         |
| C                       | c, h                   |         |
| C++                     | cpp, hpp, cc, hh, c++, h++, cxx, hxx |   |
| C/AL                    | cal                    |         |
| Cache Object Script     | cos, cls               |         |
| CMake                   | cmake, cmake.in        |         |
| COBOL                   | cobol, standard-cobol   | [highlightjs-cobol](https://github.com/otterkit/highlightjs-cobol) |
| Coq                     | coq                    |         |
| CSP                     | csp                    |         |
| CSS                     | css                    |         |
| Cap’n Proto             | capnproto, capnp       |         |
| Chaos                   | chaos, kaos            | [highlightjs-chaos](https://github.com/chaos-lang/highlightjs-chaos) |
| Chapel                  | chapel, chpl           | [highlightjs-chapel](https://github.com/chapel-lang/highlightjs-chapel) |
| Cisco CLI               | cisco                  | [highlightjs-cisco-cli](https://github.com/BMatheas/highlightjs-cisco-cli) |
| Clojure                 | clojure, clj           |         |
| CoffeeScript            | coffeescript, coffee, cson, iced | |
| CpcdosC+                | cpc                    | [highlightjs-cpcdos](https://github.com/SPinti-Software/highlightjs-cpcdos) |
| Crmsh                   | crmsh, crm, pcmk       |         |
| Crystal                 | crystal, cr            |         |
| cURL                    | curl                   | [highlightjs-curl](https://github.com/highlightjs/highlightjs-curl) |
| Cypher (Neo4j)          | cypher                 | [highlightjs-cypher](https://github.com/highlightjs/highlightjs-cypher) |
| D                       | d                      |         |
| Dafny                   | dafny                  | [highlightjs-dafny](https://github.com/ConsenSys/highlightjs-dafny)|
| Dart                    | dart                   |         |
| Delphi                  | dpr, dfm, pas, pascal  |         |
| Diff                    | diff, patch            |         |
| Django                  | django, jinja          |         |
| DNS Zone file           | dns, zone, bind        |         |
| Dockerfile              | dockerfile, docker     |         |
| DOS                     | dos, bat, cmd          |         |
| dsconfig                | dsconfig               |         |
| DTS (Device Tree)       | dts                    |         |
| Dust                    | dust, dst              |         |
| Dylan                   | dylan                  | [highlightjs-dylan](https://github.com/highlightjs/highlightjs-dylan) |
| EBNF                    | ebnf                   |         |
| Elixir                  | elixir                 |         |
| Elm                     | elm                    |         |
| Erlang                  | erlang, erl            |         |
| Excel                   | excel, xls, xlsx       |         |
| Extempore               | extempore, xtlang, xtm | [highlightjs-xtlang](https://github.com/highlightjs/highlightjs-xtlang) |
| F#                      | fsharp, fs             |         |
| FIX                     | fix                    |         |
| Flix                    | flix                   | [highlightjs-flix](https://github.com/flix/highlightjs-flix) |
| Fortran                 | fortran, f90, f95      |         |
| FunC                    | func                   | [highlightjs-func](https://github.com/highlightjs/highlightjs-func) |
| G-Code                  | gcode, nc              |         |
| Gams                    | gams, gms              |         |
| GAUSS                   | gauss, gss             |         |
| GDScript                | godot, gdscript        | [highlightjs-gdscript](https://github.com/highlightjs/highlightjs-gdscript) |
| Gherkin                 | gherkin                |         |
| Glimmer and EmberJS     | hbs, glimmer, html.hbs, html.handlebars, htmlbars | [highlightjs-glimmer](https://github.com/NullVoxPopuli/highlightjs-glimmer) |
| GN for Ninja            | gn, gni                | [highlightjs-GN](https://github.com/highlightjs/highlightjs-GN) |
| Go                      | go, golang             |         |
| Grammatical Framework   | gf                     | [highlightjs-gf](https://github.com/johnjcamilleri/highlightjs-gf) |
| Golo                    | golo, gololang         |         |
| Gradle                  | gradle                 |         |
| GraphQL                 | graphql                |         |
| Groovy                  | groovy                 |         |
| GSQL                    | gsql                   | [highlightjs-gsql](https://github.com/DanBarkus/highlightjs-gsql) |
| HTML, XML               | xml, html, xhtml, rss, atom, xjb, xsd, xsl, plist, svg | |
| HTTP                    | http, https            |         |
| Haml                    | haml                   |         |
| Handlebars              | handlebars, hbs, html.hbs, html.handlebars        | |
| Haskell                 | haskell, hs            |         |
| Haxe                    | haxe, hx               |         |
| High-level shader language| hlsl                | [highlightjs-hlsl](https://github.com/highlightjs/highlightjs-hlsl) |
| Hy                      | hy, hylang             |         |
| Ini, TOML               | ini, toml              |         |
| Inform7                 | inform7, i7            |         |
| IRPF90                  | irpf90                 |         |
| JSON                    | json                   |         |
| Java                    | java, jsp              |         |
| JavaScript              | javascript, js, jsx    |         |
| Jolie                   | jolie, iol, ol         | [highlightjs-jolie](https://github.com/xiroV/highlightjs-jolie) |
| Julia                   | julia, julia-repl      |         |
| Kotlin                  | kotlin, kt             |         |
| LaTeX                   | tex                    |         |
| Leaf                    | leaf                   |         |
| Lean                    | lean                   | [highlightjs-lean](https://github.com/leanprover-community/highlightjs-lean) |
| Lasso                   | lasso, ls, lassoscript |         |
| Less                    | less                   |         |
| LDIF                    | ldif                   |         |
| Lisp                    | lisp                   |         |
| LiveCode Server         | livecodeserver         |         |
| LiveScript              | livescript, ls         |         |
| LookML                  | lookml                 | [highlightjs-lookml](https://github.com/spectacles-ci/highlightjs-lookml) |
| Lua                     | lua                    |         |
| Macaulay2               | macaulay2              | [highlightjs-macaulay2](https://github.com/d-torrance/highlightjs-macaulay2) |
| Makefile                | makefile, mk, mak, make |        |
| Markdown                | markdown, md, mkdown, mkd |      |
| Mathematica             | mathematica, mma, wl   |         |
| Matlab                  | matlab                 |         |
| Maxima                  | maxima                 |         |
| Maya Embedded Language  | mel                    |         |
| Mercury                 | mercury                |         |
| mIRC Scripting Language | mirc, mrc              | [highlightjs-mirc](https://github.com/highlightjs/highlightjs-mirc) |
| Mizar                   | mizar                  |         |
| MKB                     | mkb                    | [highlightjs-mkb](https://github.com/Dereavy/highlightjs-mkb) |
| MLIR                    | mlir                   | [highlightjs-mlir](https://github.com/highlightjs/highlightjs-mlir) |
| Mojolicious             | mojolicious            |         |
| Monkey                  | monkey                 |         |
| Moonscript              | moonscript, moon       |         |
| N1QL                    | n1ql                   |         |
| NSIS                    | nsis                   |         |
| Never                   | never                  | [highlightjs-never](https://github.com/never-lang/highlightjs-never) |
| Nginx                   | nginx, nginxconf       |         |
| Nim                     | nim, nimrod            |         |
| Nix                     | nix                    |         |
| Oak                     | oak                    | [highlightjs-oak](https://github.com/timlabs/highlightjs-oak) |
| Object Constraint Language | ocl                 | [highlightjs-ocl](https://github.com/nhomble/highlightjs-ocl)        |
| OCaml                   | ocaml, ml              |         |
| Objective C             | objectivec, mm, objc, obj-c, obj-c++, objective-c++ |    |
| OpenGL Shading Language | glsl                   |         |
| OpenSCAD                | openscad, scad         |         |
| Oracle Rules Language   | ruleslanguage          |         |
| Oxygene                 | oxygene                |         |
| PF                      | pf, pf.conf            |         |
| PHP                     | php                    |         |
| Papyrus                 | papyrus, psc           |[highlightjs-papyrus](https://github.com/Pickysaurus/highlightjs-papyrus)    |
| Parser3                 | parser3                |         |
| Perl                    | perl, pl, pm           |         |
| Pine Script             | pine, pinescript       | [highlightjs-pine](https://github.com/jeyllani/highlightjs-pine) |
| Plaintext               | plaintext, txt, text   |         |
| Pony                    | pony                   |         |
| PostgreSQL & PL/pgSQL   | pgsql, postgres, postgresql |    |
| PowerShell              | powershell, ps, ps1    |         |
| Processing              | processing             |         |
| Prolog                  | prolog                 |         |
| Properties              | properties             |         |
| Protocol Buffers        | protobuf               |         |
| Puppet                  | puppet, pp             |         |
| Python                  | python, py, gyp        |         |
| Python profiler results | profile                |         |
| Python REPL             | python-repl, pycon     |         |
| Q#                      | qsharp                 | [highlightjs-qsharp](https://github.com/fedonman/highlightjs-qsharp) |
| Q                       | k, kdb                 |         |
| QML                     | qml                    |         |
| R                       | r                      |         |
| Razor CSHTML            | cshtml, razor, razor-cshtml | [highlightjs-cshtml-razor](https://github.com/highlightjs/highlightjs-cshtml-razor) |
| ReasonML                | reasonml, re           |         |
| Rebol & Red             | redbol, rebol, red, red-system | [highlightjs-redbol](https://github.com/oldes/highlightjs-redbol) |
| RenderMan RIB           | rib                    |         |
| RenderMan RSL           | rsl                    |         |
| RiScript                | risc, riscript         | [highlightjs-riscript](https://github.com/highlightjs/highlightjs-riscript) |
| Roboconf                | graph, instances       |         |
| Robot Framework         | robot, rf              | [highlightjs-robot](https://github.com/highlightjs/highlightjs-robot) |
| RPM spec files          | rpm-specfile, rpm, spec, rpm-spec, specfile | [highlightjs-rpm-specfile](https://github.com/highlightjs/highlightjs-rpm-specfile) |
| Ruby                    | ruby, rb, gemspec, podspec, thor, irb | |
| Rust                    | rust, rs               |         |
| RVT Script              | rvt, rvt-script        | [highlightjs-rvt-script](https://github.com/Sopitive/highlightjs-rvt-script) |
| SAS                     | SAS, sas               |         |
| SCSS                    | scss                   |         |
| SQL                     | sql                    |         |
| STEP Part 21            | p21, step, stp         |         |
| Scala                   | scala                  |         |
| Scheme                  | scheme                 |         |
| Scilab                  | scilab, sci            |         |
| Shape Expressions       | shexc                  | [highlightjs-shexc](https://github.com/highlightjs/highlightjs-shexc) |
| Shell                   | shell, console         |         |
| Smali                   | smali                  |         |
| Smalltalk               | smalltalk, st          |         |
| SML                     | sml, ml                |         |
| Solidity                | solidity, sol          | [highlightjs-solidity](https://github.com/highlightjs/highlightjs-solidity) |
| Splunk SPL              | spl                    | [highlightjs-spl](https://github.com/swsoyee/highlightjs-spl) |
| Stan                    | stan, stanfuncs        |         |
| Stata                   | stata                  |         |
| Structured Text         | iecst, scl, stl, structured-text | [highlightjs-structured-text](https://github.com/highlightjs/highlightjs-structured-text) |
| Stylus                  | stylus, styl           |         |
| SubUnit                 | subunit                |         |
| Supercollider           | supercollider, sc      | [highlightjs-supercollider](https://github.com/highlightjs/highlightjs-supercollider) |
| Svelte                  | svelte                 | [highlightjs-svelte](https://github.com/AlexxNB/highlightjs-svelte) |
| Swift                   | swift                  |         |
| Tcl                     | tcl, tk                |         |
| Terraform (HCL)         | terraform, tf, hcl     | [highlightjs-terraform](https://github.com/highlightjs/highlightjs-terraform) |
| Test Anything Protocol  | tap                    |         |
| Thrift                  | thrift                 |         |
| Toit                    | toit                   | [toit-highlight](https://github.com/snxx-lppxx/toit-highlight) |
| TP                      | tp                     |         |
| Transact-SQL            | tsql                   | [highlightjs-tsql](https://github.com/highlightjs/highlightjs-tsql) |
| Twig                    | twig, craftcms         |         |
| TypeScript              | typescript, ts, tsx    |         |
| Unicorn Rails log       | unicorn-rails-log      | [highlightjs-unicorn-rails-log](https://github.com/sweetppro/highlightjs-unicorn-rails-log) |
| VB.Net                  | vbnet, vb              |         |
| VBA                     | vba                    | [highlightjs-vba](https://github.com/dullin/highlightjs-vba) |
| VBScript                | vbscript, vbs          |         |
| VHDL                    | vhdl                   |         |
| Vala                    | vala                   |         |
| Verilog                 | verilog, v             |         |
| Vim Script              | vim                    |         |
| X#                      | xsharp, xs, prg        | [highlightjs-xsharp](https://github.com/InfomindsAg/highlightjs-xsharp) |
| X++                     | axapta, x++            |         |
| x86 Assembly            | x86asm                 |         |
| XL                      | xl, tao                |         |
| XQuery                  | xquery, xpath, xq      |         |
| YAML                    | yml, yaml              |         |
| ZenScript               | zenscript, zs          |[highlightjs-zenscript](https://github.com/highlightjs/highlightjs-zenscript) |
| Zephir                  | zephir, zep            |         |"""

aliases_formatter = '''#app-mount pre code[class~="{}" i]:before'''
final_formatter = '''{aliases_text} {{
  content: "{lang_text}";
}}'''
output = []

for line in languages.split('\n'):
    match = pattern.search(line)
    if not match:
        print("error", line)
        continue

    lang_name = match[1].strip()
    aliases = [alias.strip() for alias in match[2].split(',')]

    aliases_text = ', '.join(aliases_formatter.format(alias) for alias in aliases)
    output.append(final_formatter.format(lang_text=lang_name, aliases_text=aliases_text))

for lang_name, aliases in extras:
    aliases_text = ', '.join(aliases_formatter.format(alias) for alias in aliases)
    output.append(final_formatter.format(lang_text=lang_name, aliases_text=aliases_text))

with open("lang.css", 'w') as f:
    f.write('\n'.join(output))
