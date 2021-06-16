from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import argparse


def img_to_csv(fin=None, fout="result.csv", plot=False, noise=0, haze=0, sh=20):
	image = np.asarray(Image.open(fin))
	w, h = image.shape[0], image.shape[1]
	px_list = []
	for i in range(w):
		for j in range(h):
			if (int(image[i][j][0]) + int(image[i][j][1]) + int(image[i][j][2]) != 765):
				density = 0.9  # TODO parameter
				if np.random.uniform(0, 1) > density:
					px_list.append([j / sh, (w - i) / sh])
					if noise:
						px_list[-1][0] += np.random.uniform(-noise, noise)
						px_list[-1][1] += np.random.uniform(-noise, noise)
	for _ in range(haze):
		px_list.append([np.random.uniform(0, h/sh), np.random.uniform(0, w/sh)])
	px_list = np.array(px_list, dtype=np.float32)
	with open(fout, "w") as out:
		np.savetxt(out, px_list, fmt="%f", delimiter=",")
	if plot:
		plt.scatter(px_list[:, 0], px_list[:, 1], c="k", s=0.1)
		plt.xlim([0, h/sh])
		plt.ylim([0, w/sh])
		plt.axis("scaled")
		plt.show()
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Convert b/w image to csv")
	parser.add_argument("--fin", "-i", help="input image filename")
	parser.add_argument("--fout", "-o", default="result.csv", help="output csv filename")
	parser.add_argument("--plot", "-p", default=False, help="plot the result [1/0]")
	parser.add_argument("--noise", "-n", default=0, help="noise amount (float)")
	parser.add_argument("--haze", "-z", default=0, help="amount of noize all around the image (int)")
	parser.add_argument("--shrink", "-s", default=1, help="shrinkage coefficient (float)")
	args = parser.parse_args()
	if args.fin is None:
		raise ValueError("No input file specified")
	if args.shrink == 0:
		raise ValueError("Shrinkage coefficient cannot be a zero")
	img_to_csv(args.fin, args.fout, bool(args.plot), float(args.noise), int(args.haze), float(args.shrink))
