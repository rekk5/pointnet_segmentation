import open3d as o3
from shapenet_dataset import ShapenetDataset

sample_dataset = ShapenetDataset('/home/t/Desktop/work/pointnet/shapenetcore_partanno_segmentation_benchmark_v0', npoints=20000, split='train', classification=False, normalize=False)

points, seg = sample_dataset[4000]


pcd = o3.geometry.PointCloud()
pcd.points = o3.utility.Vector3dVector(points)
pcd.colors = o3.utility.Vector3dVector(read_pointnet_colors(seg.numpy()))

o3.visualization.draw_plotly([pcd])