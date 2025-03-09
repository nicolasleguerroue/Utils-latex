The AcroTeX eDucation Bundle (AeB)
Author: D. P. Story 
Dated: 2021-10-03

AeB contains the following:

1) web Package: Extensive support for page design.

2) exerquiz Package: Support for creating online interactive exercises and
   quizzes.

3) eforms Package: Extensive support for Acrobat forms and links

4) dljslib package: A package of JavaScript functions that extends the
   capability of exerquiz.

5) taborder package: Supports the create of a tab order for form fields.

6) Documentation for AeB (AcroTeX eDucatation Bundle) and eforms
   (including insdljs and dljslib).

What's New (2021-10-03) 
  exerquiz: In recent versions of AA/AR DC, the rollover display 
    for choice fields (radio fields and checkboxes) has changed. Previously 
    when the mouse rolls over a choice field, the tool tip is displayed. For 
    quizzes, the choice fields have no tool tip, so nothing was displayed. 
    Now, AA/AR DC displays `<tool-tip>: export-value>', which reveals 
    information not intended for the student taking that quiz. The exerquiz 
    package is modified to reflect this change. The rollover of radio buttons 
    and check boxes now displays as `Choice: a', `Choice: b', etc. The word 
    `Choice' is the tool tip and lower case letter is the export value. The 
    tool tip for all choice fields of a quizzes can be changed with 
    \TUChoice{<text>}, the default is \TUChoice{Choice}.

What's New (2021-06-19) Move files out of this distribution to the 
  acrotex-js package, dated 2021/06/19 or later. The folder JavaScript
  file aeb.js (and aeb_pro.js) are now distributed with acrotex-js. Installation
  instructions are now included with that package.

What's New (2021-05-29)
  exerquiz: Internal changes to Begin Quiz and End Quiz actions to
    support eq-pin2corr package. Exerquiz now tracks duplication quiz names. 
    Shift-Begin Quiz now clears the quiz without initializing it. 

What's New (2021-05-15) 
  exerquiz: Some bug fixes. 
    Defined the new insertAt key of the \bChoices command. See
    http://www.acrotex.net/blog/?tag=enhanced-quizzes for discussion 
    and demo files.

What's New (2021-05-10) 
  web: added navibar* option
  exerquiz: new option usealtadobe is passed to insdljs
      new option userbmintrvl, see http://www.acrotex.net/blog/?p=1482
      shortquiz: Enhanced user experience, see http://www.acrotex.net/blog/?p=1489
      and http://www.acrotex.net/blog/?p=1493.
      
  Other new demo files: 
      eqexam: A Matching-type Problem: http://www.acrotex.net/blog/?p=1457
      exerquiz
        Matching-type questions: http://www.acrotex.net/blog/?p=1446
        Randomized matching-type questions: http://www.acrotex.net/blog/?p=1449                
        A spell checking feature: http://www.acrotex.net/blog/?p=1437
      insdljs: Exploring the defineJS environment: http://www.acrotex.net/blog/?p=1442
        
What's New (2021-04-24)
  exerquiz: Options usemcfi and userbmintrvl, bug fixes.
  dljslib: Revised useGermanNums, created alias of useDeNums, see http://www.acrotex.net/blog/?p=1039
    new option useEnNums, a companion to useDeNums, http://www.acrotex.net/blog/?p=1470

What's New (2021-02-28) exerquiz: bug fix to \rbtAAKey. web: removed legacy code.

What's New (2021-02-17) exerquiz: Added an optional fourth argument to the JavaScript
    function DisplayQuizResults(), this is in support of the eq-pin2corr 
    package.
    
What's New (2021-02-21) Bug fixes

What's New (2021-02-07) Minor change in the defineJS environment that is 
  critical to a fix in the page events environments of aeb_pro.

What's New (2021-02-04) Updated documentation to reflect security changes
  in Acrobat, authored acrobat-in-workflow.pdf to distribute with the AeB. 

What's New (2021-01-20) Defined two commands \doNotRandomizeChoices
  and \allowRandomizedChoices; these turn off and turn on the randomization
  of choices in MC and MS questions.

What's New (2020-12-30) 
  exerquiz: Minor bug fixes; converted some inline JS to JS in 
    the defineJS env. 
  eforms: New keys for option list of form macros: \rectW, \rectH,
    \width, \height, \scalefactor. Also introduced are \textFontDefault,
    \textSizeDefault, and \btnSpcr. All form fields and link annotations
    now obey \pdfSpacesOn (and \pdfSpacesOff).
  insdljs: Added \Thread and \Launch actions; \dfnJSCR and \dfnJSCRDef.
    New options of defineJS: \makecmt and \typeset. Improved the defineJS
    environment. Refer to http://www.acrotex.net/blog/?p=1442
    for a full discussion of the defineJS and all its features.
    
What's New (2020-11-20) Fixed minor, yet critical, bug converning duplicate
definition of \URI.

What's New (2020-11-11) Added new command \SpellCheck, to check the spelling 
of a fill-in question (exerquiz). Added width, height, scalefactor keys to 
form fields to rescale fields (eforms). 

What's New (2020-03-14) Minor changes that support new features of eqexam.

What's New (2020-01-01) Replace use of \count0 with new counter \eqtmpcnta, 
in situation, the value of \count0 was leaking out giving incorrect page 
numbers. 

What's New (2019-12-17) Defined \InputExrSolnsLevel and \InputQzSolnsLevel to
make it easy to change the section-type for the solution pages.

What's New (2019-08-13) Use \protect when formatting a enhanced preview value.
Other minor changes and bug fixes.

What's New (2019-05-24) Added the enhanced preview feature. When in effect 
along with ordinary preview, captions of buttons and initial values of other 
fields are viewable in non-conforming PDF readers. 

What's New (2019/03/16) minor bug fixes; added \bParams/\eParams command pair 
to pass arguments to JS code snippets declared within the defineJS 
environment. Fixed the spacing problem when dvips is used to compile a doc 
containing the defineJS environment. 

What's New (2018/12/13) More changes in exerquiz to support mi-solns; misc. bug fixes.

What's New (2028/12/05) Some changes in exerquiz to support mi-solns. Require aeb-comment
(version 3.2 of comment.sty). The newer versions of comment.sty are incompatible with
eqexam (which is supported by exerquiz) and introduces spurious spaces.

What's New (2018/11/27) Some changes to eforms package to support the new icon-appr
package.

What's New (2018/08/16) Changes to eforms and insdljs: several keys (eforms) added to
support aeb_mlink and annot_pro; switch add to insdljs to detect whether document JS
has been included.

What's New (2018/03/22) Changes in eforms to support features of aeb_mlink. Minor bug fixes

What's New (2018/02/13) Added commands to optionally group each solution when the appear
at the end of the file; this applies both exercises and quizzes.

What's New (2017/09/06) Suggested new problem type: "Correcting a math problem", see
http://www.acrotex.net/blog/?p=1335 for a demo. Better compatibility with luatex. Minor
bug fixes.

What's New (2017-08-08) Support for multi-letter variables, alternate appearances,
and interval repetition. The demo file for these features is
http://www.acrotex.net/blog/?p=1330

Examples for AeB have been moved to
http://www.math.uakron.edu/~dpstory/webeq_ex.html, another copy
of the examples are at http://www.acrotex.net/blog/?cat=89

Additional examples are posted on the AcroTeX Blog page
http://www.acrotex.net/blog/

Now, I simply must get back to my retirement.

D. P. Story
www.acrotex.net
dpstory at uakron dot edu
dpstory at acrotex dot net
