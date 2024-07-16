import open3d as o3d

# Load the point cloud file
pcd_path = "/home/t/Desktop/work/pointnet/full_predicted.pcd"  # Update this path to your actual PCD file path
pcd = o3d.io.read_point_cloud(pcd_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])