const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {parse} = require('../scripts/floating_toc_callouts.js');
const heading = (text, line, level=2) => ({heading:text,level,position:{start:{line,col:0,offset:0},end:{line,col:text.length,offset:text.length}}});

test('flat callout-only notes support metadata, fold flags and duplicate titles',()=>{
 const text='> [!concept-proposition] 命题一\n> 正文\n\n> [!claim] Smith\n> 正文\n\n> [!claim] Smith\n> [!warning|limits]- 适用局限';
 const rows=parse(text);
 assert.deepEqual(rows.map(x=>[x.heading,x.level,x.position.start.line]),[['命题一',2,0],['Smith',2,3],['Smith',2,6],['适用局限',2,7]]);
 assert.equal(rows[3].position.start.offset,text.indexOf('> [!warning'));
});
test('code fences, YAML, comments, nested cards and decorative markers are excluded',()=>{
 const text=['---','summary: |','  > [!warning] YAML','---','%%','> [!claim] comment','%%','```md','> [!claim] code','```','> [!debates] 学术争议','> > [!axis] nested','> ```md','> [!claim] quoted code','> ```','> [!empirical-divider]','> [!line-a] auxiliary','%% > [!claim] inline %%','> [!warning] visible'].join('\n');
 assert.deepEqual(parse(text).map(x=>x.heading),['学术争议','visible']);
});
test('native headings remain immutable and callouts follow their actual heading level',()=>{
 const native=[heading('Section',0),heading('Subsection',3,3)];
 const before=JSON.stringify(native);
 const rows=parse('## Section\n> [!claim] A\n\n### Subsection\n> [!claim] B',native);
 assert.deepEqual(rows.map(x=>[x.heading,x.level]),[['Section',2],['A',3],['Subsection',3],['B',4]]);
 assert.equal(JSON.stringify(native),before);
 rows[0].position.start.line=90;
 assert.equal(native[0].position.start.line,0);
});
test('template placeholders survive HTML rendering, and missing titles have useful names',()=>{
 assert.deepEqual(parse('> [!claim] <Lastname, I.>\n> [!question]\n> [!concept-lens|notitle] 概念透镜').map(x=>x.heading),['&lt;Lastname, I.&gt;','研究问题','概念透镜']);
});
test('the real concept template exposes propositions at the same level as other cards',()=>{
 const text=fs.readFileSync('wiki/templates/template-concept.md','utf8');
 const rows=parse(text);
 assert.equal(rows.filter(x=>x.__ftocCallout==='concept-proposition').length,2);
 assert(rows.every(x=>x.level===2));
 assert(!rows.some(x=>x.heading==='围绕概念形成的命题'||x.__ftocCallout.endsWith('-divider')));
 assert(rows.some(x=>x.heading==='适用局限'));
});
