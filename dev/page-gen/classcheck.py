import re, sys
css = open(sys.argv[1]).read()
def esc(c):
    return re.sub(r'([^a-zA-Z0-9_-])', r'\\\1', c)
missing = set()
for f in sys.argv[2:]:
    h = open(f).read()
    main = h[h.find('<main'):]
    for cl in re.findall(r'class="([^"]*)"', main):
        for c in cl.split():
            e = esc(c)
            if c.startswith('lucide') or c in ('group',): continue
            if re.match(r'^\d', c): e = '\\3' + c[0] + ' ' + esc(c[1:])
            if ('.' + e) not in css: missing.add(c)
print(sorted(missing))
