# 数据合并 （data-merge）

提醒：本文件不建议使用文本编辑器查看，推荐直接在 GitHub 上查看预览。

## 问题背景

第二个大作业马上就要布置了，<ruby>续老师<rt>鸽王</rt></ruby> 因为忙于备课并没有时间准备数据，杰哥和 Harry 也正被 Vivado 折磨得死去活来。然而要是周五前没法准备好数据，就要出教学事故了，焦头烂额的他们想要找一个人帮忙。然而，芃芃已经愉快地踏上了[前往霓虹国的旅程](https://mp.weixin.qq.com/s/wK7jq2TbwO4lEOYz2q1DNQ)。无奈之下，他们把目光转向了你……

## 问题描述

你的需要完成以下的设计：

1. 一个 Python 程序 `merge.py`，接受两个参数 `input_file` 和 `output_file`，按照下列要求完成数据合并
2. 一份 `Makefile`，它能够自动对 `data` 目录下所有形如 `*.in.h5` 的文件运行上面的程序，输出路径为同一目录下的 `*.out.h5`，并且具有一个 `clean` 目标，删除所有输出文件。

### 输入格式

输入数据为 PMT 题目的训练数据，储存在 HDF5 文件中，其中有三个表：`TriggerInfo` 保存触发的时间戳信息；`Waveform` 保存波形信息；`GroundTruth` 保存每个光子的击中时间，即标签信息。每个表都有对应的事例编号或通道编号，如下所示。如果需要了解具体物理背景或者更详细的解释，你可以参照 [tpl_PMT-waveform](https://github.com/physics-data/tpl_PMT-waveform) 仓库的说明。

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

你需要将上面三张表中的内容合并为输出文件中的一张表 `PMTInfo` ，共有 6 列：`EventID`, `ChannelID`, `Sec`, `NanoSec`, `Waveform`, `PETime`，意义与数据类型与上面相同。请注意，每行的五元组 `(EventID, ChannelID, Sec, NanoSec, Waveform)` （即一次事件中一个探测器对应的波形） 可能对应任意多个 `PETime` （即真正的闪烁时间）；这张表中的每一行表征了一次闪烁的所有信息，因此行数以及 `PETime` 一列的内容与顺序应该与 `GroundTruth` 表**完全一致**。

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

## 数据与评分

本次评分的数据全部下发，位于 `data` 目录下，共 10 组。最终分数构成如下：

1. 正确性测试 80 分：每组数据 8 分，只当你的输出与答案中的数据**完全一致**时才得分
2. `Makefile` 10 分：正确书写通用规则，能够不重复、不遗漏地调用脚本执行任务，并能够使用 `clean` 删除输出文件
3. 白盒 10 分：代码风格 5 分、Git 使用 5 分

你可以调用 `grade.py` 来获取你的本地评分。

## 提示

1. 你应该使用 `pandas` 的 `DataFrame` 组件来处理这些数据，并进行 `join` 等操作。
2. 由于数据可能较大，写入输出时请启用 `h5py` 的透明压缩功能（可自行查询）。
3. 本作业的目的是为了让大家熟悉 `pandas` 的使用，因此最终生成了带有大量冗余数据的格式，这严重违反了数据处理的*一次原则*，请**不要**在实际场景中使用这样的数据存储方法。
