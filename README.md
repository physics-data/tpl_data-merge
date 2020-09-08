# 数据合并 （data-merge）

提醒：本文件不建议使用文本编辑器查看，推荐直接在 GitHub 上查看预览。

## 问题背景

去年的第二个大作业马上就要布置了，<ruby>续老师<rt>鸽王</rt></ruby> 因为忙于备课并没有时间准备数据，杰哥和 Harry 也正被 Vivado （今年不知道是啥）折磨得死去活来。然而要是周五前没法准备好数据，就要出教学事故了，焦头烂额的他们想要找一个人帮忙。然而，天才少年爱迪生并不在教学团队中。无奈之下，他们把目光转向了你……

## 问题描述

你的需要完成以下的设计：

1. 一个 R 程序 `merge.R`，接受两个参数 `input_file` 和 `output_file`，按照下列要求完成数据合并
2. 一份 `Makefile`，它能够自动对 `data2` 目录下所有形如 `*.in.Rdata` 的文件运行上面的程序，输出路径为同一目录下的 `*.out.Rdata`，并且具有一个 `clean` 目标，删除所有输出文件。

### 输入格式

输入数据为 PMT 题目的训练数据，储存在 Rdata 文件中，其中有两个表：`TriggerInfo` 保存触发的时间戳信息；`GroundTruth` 保存每个光子的击中时间，即标签信息。每个表都有对应的事例编号或通道编号，如下所示。如果需要了解具体物理背景或者更详细的解释，你可以参照 [tpl_PMT-waveform](https://github.com/physics-data/tpl_PMT-waveform) 仓库的说明。

<div markdown="0" align="center">
    <table cellspacing="0" border="0">
        <colgroup width="180"></colgroup>
        <colgroup width="180"></colgroup>
        <colgroup width="180"></colgroup>
        <tr>
            <td style="border-bottom: 2px solid #000000" colspan="3" align="center" valign="middle"><b><i><font color="#000000">TriggerInfo</font></i></b></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><b><font color="#000000">EventID</font></b> (int64)</td>
            <td align="center" valign="middle"><b><font color="#000000">Sec</font></b> (int32)</td>
            <td align="center" valign="middle"><b><font color="#000000">NanoSec</font></b> (int32)</td>
        </tr>
        <tr>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">2</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">109000153</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">3</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">201205243</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
    </table>
    <table cellspacing="0" border="0">
        <colgroup width="180"></colgroup>
        <colgroup width="200"></colgroup>
        <colgroup width="250"></colgroup>
        <tr>
            <td style="border-bottom: 2px solid #000000" colspan="3" height="19" align="center" valign="middle"><b><i><font color="#000000">Waveform</font></i></b></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle"><b><font color="#000000">EventID</font></b> (int64)</td>
            <td align="center" valign="middle"><b><font color="#000000">ChannelID</font></b> (int16)</td>
            <td align="center" valign="middle"><b><font color="#000000">Waveform</font></b> (int16 [1029])</td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="0" sdnum="1033;"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">974, 973, …, 972</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">973, 974, …, 975</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="2" sdnum="1033;"><font color="#000000">2</font></td>
            <td align="center" valign="middle"><font color="#000000">973, 973, …, 974</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
    </table>
    <table cellspacing="0" border="0">
        <colgroup width="180"></colgroup>
        <colgroup width="200"></colgroup>
        <colgroup width="180"></colgroup>
        <tr>
            <td style="border-bottom: 2px solid #000000" colspan="3" height="19" align="center" valign="middle"><b><i><font color="#000000">GroundTruth</font></i></b></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle"><b><font color="#000000">EventID</font></b> (int64)</td>
            <td align="center" valign="middle"><b><font color="#000000">ChannelID</font></b> (int16)</td>
            <td align="center" valign="middle"><b><font color="#000000">PETime</font></b> (int16)</td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="0" sdnum="1033;"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">269</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">284</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle" sdval="2" sdnum="1033;"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">287</font></td>
        </tr>
        <tr>
            <td height="18" align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
    </table>
</div>

### 输出格式

你需要将上面两张表中的内容合并为输出文件中的一张表 `PMTInfo` ，共有 5 列：`EventID`, `ChannelID`, `Sec`, `NanoSec`, `PETime`。

<div markdown="0" align="center">
    <table cellspacing="0" border="0">
        <tr>
            <td style="border-bottom: 2px solid #000000" colspan="6" align="center" valign="middle"><b><i><font color="#000000">PMTInfo</font></i></b></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><b><font color="#000000">EventID</font></b> (int64)</td>
            <td align="center" valign="middle"><b><font color="#000000">ChannelID</font></b> (int16)</td>
            <td align="center" valign="middle"><b><font color="#000000">Sec</font></b> (int32)</td>
            <td align="center" valign="middle"><b><font color="#000000">NanoSec</font></b> (int32)</td>
            <td align="center" valign="middle"><b><font color="#000000">Waveform</font></b> (int16 [1029])</td>
            <td align="center" valign="middle"><b><font color="#000000">PETime</font></b> (int16)</td>
        </tr>
        <tr>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
            <td align="center" valign="middle"><font color="#000000">974, 973, …, 972</font></td>
            <td align="center" valign="middle"><font color="#000000">269</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
            <td align="center" valign="middle"><font color="#000000">974, 973, …, 972</font></td>
            <td align="center" valign="middle"><font color="#000000">284</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
            <td align="center" valign="middle"><font color="#000000">974, 973, …, 972</font></td>
            <td align="center" valign="middle"><font color="#000000">287</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle" sdval="1" sdnum="1033;"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
            <td align="center" valign="middle"><font color="#000000">974, 973, …, 972</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">1</font></td>
            <td align="center" valign="middle"><font color="#000000">0</font></td>
            <td align="center" valign="middle"><font color="#000000">89692193</font></td>
            <td align="center" valign="middle"><font color="#000000">973, 974, …, 975</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
        <tr>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
            <td align="center" valign="middle"><font color="#000000">…</font></td>
        </tr>
    </table>
</div>
（此表供参考）

## 数据与评分

本次评分的数据全部下发，位于 `data2` 目录下，共 10 组。最终分数构成如下：

1. 正确性测试 80 分：每组数据 8 分，只当你的输出与答案中的数据**完全一致**时才得分
2. `Makefile` 10 分：正确书写通用规则，能够不重复、不遗漏地调用脚本执行任务，并能够使用 `clean` 删除输出文件
3. 白盒 10 分：代码风格 5 分、Git 使用 5 分

你可以调用 `grade.py` 来获取你的本地评分（`grade.R`只供内部使用）。

## 提示

3. 本作业的目的是为了让大家熟悉数据的处理，因此最终生成了带有大量冗余数据的格式，这严重违反了数据处理的*一次原则*，请**不要**在实际场景中使用这样的数据存储方法。
