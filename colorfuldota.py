# Colored dota texter
import sys, re

def main():
	colordict = {"olive":"\x10","pink":"\x11","red":"\x12","orange":"\x13","darkyellow":"\x14","lightgreen":"\x15","purple":"\x16","grey":"\x17","green":"\x18","blue":"\x19","white":"\x0B","limegreen":"\x0C","hotpink":"\x0E","violet":"\x1A","magenta":"\x1C","yellow":"\x1F"}
	if len(sys.argv) != 2:
		print("Call like 'python ./dotacolor.py \"YOUR STRING[[colorname]]STRING IN COLOR\"' Include the quotes. Copy the output into the game (on Windows, select and right-click)")
		print("Color names:")
		for key, value in colordict.items():
			print(key)
		return -1

	entrytext = sys.argv[1]
	outtext = re.sub('\[\[(.*?)]\]',lambda x: colordict[x.group(0)[2:-2]], entrytext, flags=re.DOTALL)
	print(outtext)

if __name__ == "__main__":
	main()
