# gzdoom-vuln
after a few days and many gummy bear vitamins i've decided to release my research. enjoy!

## this vulnerability does *NOT* seem to affect macOS or Linux.

few days ago i was bored and decided to fuzz my favorite DOOM source-port, GZDoom. this is one of many.

i'm not all that great at C or C++ early. but it seems that the culprit would be this function, outlined below. (also kindly outlined by both IDA and the Debug build!)

![seh](https://i.imgur.com/WUk4vg2.png)

```C

FTexture *IMGZTexture_TryCreate(FileReader & file, int lumpnum)
{
	uint32_t magic = 0;
	uint16_t w, h;
	int16_t l, t;
	bool ispalette;

	file.Seek(0, FileReader::SeekSet);
	if (file.Read(&magic, 4) != 4) return NULL;
	if (magic != MAKE_ID('I','M','G','Z')) return NULL;
	w = file.ReadUInt16();
	l = file.ReadInt16();
	h = file.ReadUInt16();
	t = file.ReadInt16();
	ispalette = checkIMGZPalette(file);
	return new FIMGZTexture(lumpnum, w, h, l, t, !ispalette);
}

```
from my few days of debugging, using tools designed for working with .WAD files and whatnot, there's a fair conclusion that lumps are being processed incorrectly. 

in one example, i used wadext on a crashing wad and it ended up creating a 1.1 GB .lmp file filled with 0. wonderful.

this would seem like a rather mundane bug, if it wasn't for the fact that i was able to get partial control over $rip and control over $rsp. $rsb is on it's own, doing jack knows what.
here's a few screenshots for a more visual representation, per IDA.

Control over $rsp but not yet $rip (note how $rbp just sits at zero - the few times it wasn't it tried to access invalid memory): 

![img1](https://i.imgur.com/EgztIKi.png)
![img2](https://i.imgur.com/LpJEQN5.png)

those random characters are generized by BFF's minimized.py script, moreover, $rip is 0x78787878, so we have partial control.

of course, you couldn't see that in the following pictures, so here:

![rip](https://i.imgur.com/6L1cual.png)

a nice tip - PEDA doesn't play too nice with windows, nor does gdbserver in my experience. quite a shame.

# What Do??



nothing, at the moment. ~~though i'd love to see a working PoC~~ HAHAHAHAHA DISREGARD THAT, WORKING POC (control over $rip, no exec yet) forwarded to the gzdoom developers.

keep on ripping and tearing, and keep an eye out for possible new releases. if you are somehow posessed by satan himself and want to donate, i accept 

BTC: 3GNr9gEmmBzAZkmxWM5GuYRd9A2wQmU9Gq

LTC: M9yybfEZeaUBbBLxqZqsGgJKNbbTeFJG5c

ETH: 0xec5d233ca4c99bdae6053fc258c0f31c5ef24690

Tools used:

* Binary Ninja
* IDA Pro
* gdb (+ gdb-peda) (on Windows, no less.)
* SLATE
* wadext
* HxD
* Kaitai Struct definition for DOOM .wad format 

$rip and tear, my friends

# Postmortem

Devs added lump size validation in to `file_wad.cpp`. Code can be seen [here](https://github.com/coelckers/gzdoom/commit/cbe4c9c5c1ea2cbb193d548e96e9902f03faa61a)

Currently working on developing code-execution exploits without NX or ASLR. See [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-exploit-guard/customize-exploit-protection) for details on how to disable these features per-process on Windows 10. 

Current state: (gzdoom-pack-exploit.py)
![img3](https://i.imgur.com/V1q0rka.png)

We're still unable to execute code, but in the end we have sufficient control over all registers; regardless of NX or ASLR.

### magic number for buffer b4 overflow seems to be 32800
