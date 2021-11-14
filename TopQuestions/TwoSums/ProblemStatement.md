{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue-Medium;\f1\fnil\fcharset0 HelveticaNeue;\f2\fmodern\fcharset0 Courier;
\f3\fnil\fcharset0 HelveticaNeue-Italic;\f4\fmodern\fcharset0 Courier-Oblique;\f5\fnil\fcharset0 HelveticaNeue-BoldItalic;
\f6\fnil\fcharset0 HelveticaNeue-Bold;\f7\fnil\fcharset0 Menlo-Bold;\f8\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red25\green25\blue25;\red255\green255\blue255;\red67\green91\blue103;
\red29\green38\blue42;\red245\green247\blue249;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c12941\c12941\c12941;\cssrgb\c100000\c100000\c100000;\cssrgb\c32941\c43137\c47843;
\cssrgb\c14902\c19608\c21961;\cssrgb\c96863\c97647\c98039;\cssrgb\c0\c0\c0\c65098;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Two Sum\
\pard\pardeftab720\sl400\partightenfactor0

\f1\b0\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf5 \cb3 \strokec5 Given an array of integers\'a0
\f2\fs26 \cf4 \cb6 \strokec4 nums
\f1\fs28 \cf5 \cb3 \strokec5 \'a0and an integer\'a0
\f2\fs26 \cf4 \cb6 \strokec4 target
\f1\fs28 \cf5 \cb3 \strokec5 , return\'a0
\f3\i indices of the two numbers such that they add up to\'a0
\f4\fs26 \cf4 \cb6 \strokec4 target
\f1\i0\fs28 \cf5 \cb3 \strokec5 .\
You may assume that each input would have\'a0
\f5\i\b exactly
\f6\i0 \'a0one solution
\f1\b0 , and you may not use the\'a0
\f3\i same
\f1\i0 \'a0element twice.\
You can return the answer in any order.\
\pard\pardeftab720\sa280\partightenfactor0

\f6\b \cf5 Example 1:
\f1\b0 \cb1 \
\pard\pardeftab720\sl400\partightenfactor0

\f7\b\fs26 \cf5 \cb6 Input:
\f8\b0  nums = [2,7,11,15], target = 9\

\f7\b Output:
\f8\b0  [0,1]\

\f7\b Output:
\f8\b0  Because nums[0] + nums[1] == 9, we return [0, 1].\
\pard\pardeftab720\sa280\partightenfactor0

\f6\b\fs28 \cf5 \cb3 Example 2:
\f1\b0 \cb1 \
\pard\pardeftab720\sl400\partightenfactor0

\f7\b\fs26 \cf5 \cb6 Input:
\f8\b0  nums = [3,2,4], target = 6\

\f7\b Output:
\f8\b0  [1,2]\
\pard\pardeftab720\sa280\partightenfactor0

\f6\b\fs28 \cf5 \cb3 Example 3:
\f1\b0 \cb1 \
\pard\pardeftab720\sl400\partightenfactor0

\f7\b\fs26 \cf5 \cb6 Input:
\f8\b0  nums = [3,3], target = 6\

\f7\b Output:
\f8\b0  [0,1]\
\pard\pardeftab720\sa280\partightenfactor0

\f1\fs28 \cf5 \cb3 \'a0\cb1 \
\pard\pardeftab720\sa280\partightenfactor0

\f6\b \cf5 \cb3 Constraints:
\f1\b0 \cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f2\fs26 \cf4 \cb6 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 2 <= nums.length <= 10
\fs19\fsmilli9750 4
\f1\fs28 \cf5 \cb1 \strokec5 \
\ls1\ilvl0
\f2\fs26 \cf4 \cb6 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 -10
\fs19\fsmilli9750 9
\fs26 \'a0<= nums[i] <= 10
\fs19\fsmilli9750 9
\f1\fs28 \cf5 \cb1 \strokec5 \
\ls1\ilvl0
\f2\fs26 \cf4 \cb6 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 -10
\fs19\fsmilli9750 9
\fs26 \'a0<= target <= 10
\fs19\fsmilli9750 9
\f1\fs28 \cf5 \cb1 \strokec5 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f6\b \cf5 \cb3 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 Only one valid answer exists.
\f1\b0 \cb1 \
\pard\pardeftab720\sa280\partightenfactor0
\cf5 \cb3 \'a0\cb1 \
\pard\pardeftab720\partightenfactor0

\f6\b \cf5 \cb3 Follow-up:\'a0
\f1\b0 Can you come up with an algorithm that is less than\'a0
\f2\fs26 \cf4 \cb6 \strokec4 O(n
\fs19\fsmilli9750 2
\fs26 )\'a0
\f1\fs28 \cf5 \cb3 \strokec5 time complexity?\cb1 \
\pard\pardeftab720\sl400\partightenfactor0

\fs26 \cf7 \strokec7 \
}