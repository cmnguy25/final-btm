import os
import folium
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImageMetadataExtractor:
    trees = [
        (44.52910492, -69.66296708),
        (44.5285084, -69.66149907),
        (44.52850618, -69.66155193),
        (44.52708022, -69.6604851),
        (44.52703379, -69.66031835),
        (44.52914165, -69.66311049),
        (44.52895813, -69.66286431),
        (44.52889891, -69.66276904),
        (44.52695925, -69.65939812),
        (44.52695747, -69.65972704),
        (44.52696951, -69.65984702),
        (44.52873426, -69.66233237),
        (44.52695331, -69.65945253),
        (44.52693091, -69.65952901),
        (44.5269353, -69.65967887),
        (44.52851935, -69.66198767),
        (44.52697606, -69.65985273),
        (44.52886774, -69.66260631),
        (44.52761212, -69.65922142),
        (44.52756173, -69.66113481),
        (44.52861747, -69.66207427),
        (44.52717084, -69.66067032),
        (44.52709623, -69.6606174),
        (44.52799245, -69.66142088),
        (44.52799982, -69.66139511),
        (44.52777806, -69.66119148),
        (44.5495593, -69.62974562),
        (44.54959471, -69.62934804),
        (44.5496406, -69.62975426),
        (44.549686, -69.6297763),
        (44.55320219, -69.62811536),
        (44.55303827, -69.6275268),
        (44.55320771, -69.62814586),
        (44.55319974, -69.62752168),
        (44.55330345, -69.6276284)
    ]
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.coordinates_list = []

    def extract_image_metadata(self, image_path):
        """
        Extracts metadata from an image file.

        Parameters:
        - image_path: str, path to the image file

        Returns:
        - metadata: dict, a dictionary containing the metadata of the image
        """
        # Open the image file
        image = Image.open(image_path)

        # Extract basic metadata using PIL
        basic_metadata = {
            "format": image.format,
            "mode": image.mode,
            "size": image.size,
            "info": image.info,
        }

        # Extract EXIF data using PIL
        exif_metadata = {}
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                exif_metadata[tag_name] = value

        # Combine basic metadata and EXIF metadata
        metadata = {
            "basic": basic_metadata,
            "exif": exif_metadata,
        }

        return metadata
    
    def extract_gps_info(self, image_path):
        with Image.open(image_path) as img:
            exif_data = img._getexif()

            if exif_data is not None:
                gps_info = {}
                time_info = None
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    if tag_name == "GPSInfo":
                        for key in value:
                            gps_tag = GPSTAGS.get(key, key)
                            gps_info[gps_tag] = value[key]
                    elif tag_name == "DateTimeOriginal":
                        time_info = value

                if gps_info:
                    latitude = gps_info.get('GPSLatitude')
                    latitude_ref = gps_info.get('GPSLatitudeRef')
                    longitude = gps_info.get('GPSLongitude')
                    longitude_ref = gps_info.get('GPSLongitudeRef')

                    if latitude and longitude and latitude_ref and longitude_ref:
                        lat_deg = latitude[0]
                        lat_min = latitude[1]
                        lat_sec = latitude[2]
                        lon_deg = longitude[0]
                        lon_min = longitude[1]
                        lon_sec = longitude[2]

                        lat = (lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)) * (-1 if latitude_ref == 'S' else 1)
                        lon = (lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)) * (-1 if longitude_ref == 'W' else 1)

                        if time_info:
                            timestamp = datetime.strptime(time_info, '%Y:%m:%d %H:%M:%S')
                            self.coordinates_list.append((lat, lon, timestamp))

    def get_coordinates_with_time(self):
        for filename in os.listdir(self.folder_path):
            if filename.upper().endswith(('_V.JPG', '_V.PNG', '_V.JPEG', '_V.BMP', '_V.GIF')):
                image_path = os.path.join(self.folder_path, filename)
                self.extract_gps_info(image_path)
        
        return sorted(self.coordinates_list, key=lambda x: x[2])

    def plot_coordinates_on_map(self, coordinates, map_file='map.html'):
        map_center = [sum(x[0] for x in coordinates) / len(coordinates), sum(x[1] for x in coordinates) / len(coordinates)]
        map_obj = folium.Map(location=map_center, zoom_start=15)

        for i, coord in enumerate(coordinates):
            folium.Marker(
                location=[coord[0], coord[1]],
                popup=f'Coordinate: ({coord[0]}, {coord[1]})',
                icon=folium.DivIcon(
                    html=f'''
                    <div style="
                        font-size: 14px; 
                        color: white; 
                        background: blue; 
                        border-radius: 50%; 
                        width: 25px; 
                        height: 25px; 
                        text-align: center;
                        line-height: 25px;
                        border: 2px solid white;">
                        {i+1}
                    </div>
                    '''
                )
            ).add_to(map_obj)

        map_obj.save(map_file)
        return map_obj
    
    def plot_tree_emoji_on_map(self, coordinates, map_file='map.html'):
        map_center = [sum(x[0] for x in coordinates) / len(coordinates), sum(x[1] for x in coordinates) / len(coordinates)]
        map_obj = folium.Map(location=map_center, zoom_start=15)

        for coord in coordinates:
            folium.Marker(
                location=[coord[0], coord[1]],
                popup=f'Coordinate: ({coord[0]}, {coord[1]})',
                icon=folium.DivIcon(
                    html=f'''
                    <div style="
                        font-size: 24px; 
                        text-align: center;
                        line-height: 24px;">
                        🌳
                    </div>
                    '''
                )
            ).add_to(map_obj)

        map_obj.save(map_file)
        return map_obj
    
    def count_trees_in_image(self, image_path):
        # Load the image
        image = Image.open(image_path)
        
        # Convert image to grayscale
        image_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

        # Use edge detection to highlight the tree trunks
        edges = cv2.Canny(image_gray, threshold1=50, threshold2=150)

        # Use contour detection to find individual tree trunks
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours on the image to visualize detected trees
        image_contours = np.array(image).copy()
        cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 3)

        # Display the image with contours
        plt.imshow(image_contours)
        plt.axis('off')
        plt.show()

        # Count the number of detected contours
        num_trees = len(contours)
        
        return num_trees
    
    def generate_random_points(self, coord, num_points, radius):
        """
        Generate a random number of points around a given coordinate within a specified radius.
        """
        # Convert radius from meters to degrees
        radius_in_degrees = radius / 111320
        
        # Generate random points
        points = []
        for _ in range(num_points):
            angle = np.random.uniform(0, 2 * np.pi)
            distance = np.random.uniform(0, radius_in_degrees)
            
            delta_lat = distance * np.cos(angle)
            delta_lon = distance * np.sin(angle)
            
            new_lat = coord[0] + delta_lat
            new_lon = coord[1] + delta_lon / np.cos(np.radians(coord[0]))  # Adjust for longitude
            points.append((new_lat, new_lon))
        
        return points

    def plot_coordinates_with_random_points_on_map(self, total, radius=30, map_file='random_points_map.html'):
        """
        Plot coordinates from the total list and random points around them within the specified radius using Folium.
        """
        all_points = []

        map_center = [sum(x[0] for x in total) / len(total), sum(x[1] for x in total) / len(total)]
        map_obj = folium.Map(location=map_center, zoom_start=15)

        for coord in total:
            num_points = 1 # np.random.randint(1, 2)
            random_points = self.generate_random_points(coord, num_points, radius)
            all_points.extend(random_points)

            # Plot the original coordinate
            folium.Marker(
                location=[coord[0], coord[1]],
                icon=folium.DivIcon(
                    html=f'''
                    <div style="
                        font-size: 14px; 
                        color: white; 
                        background: red; 
                        border-radius: 50%; 
                        width: 25px; 
                        height: 25px; 
                        text-align: center;
                        line-height: 25px;
                        border: 2px solid white;">
                        •
                    </div>
                    '''
                )
            ).add_to(map_obj)
            
            # Plot the random points
            for point in random_points:
                folium.Marker(
                    location=[point[0], point[1]],
                    icon=folium.Icon(color='blue')
                ).add_to(map_obj)

        map_obj.save(map_file)
        return map_obj
    



