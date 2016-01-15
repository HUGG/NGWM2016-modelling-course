## Data visualization with **ParaView**  - outline

#### Post-processing
- Results can be post-processed to convert to `.vtk` files by double-clicking on the `ExportDB.bat` file
  - This runs a Python code that converts the output from the default format in Gale to a `.vtk` file that can be loaded in **ParaView**
  - Note: This uses the software **VisIt** for the conversion

#### Visualizing data in **ParaView**
- Loading data files in **ParaView**
  - File -> Open...
  - Gale output files:
    1. `FEM_Grid_pressure-mesh.#####`: Pressures on the FE grid
    2. `FEM_Grid_v-mesh.#####`: Strain rates and velocities on the FE grid
    3. `materialSwarm.#####`: Various field data values on the cloud of particles, including viscosity
  - Loading one time step versus a whole series of steps
    - By default, when you select a file to load in ParaView, all time steps for the output will be loaded.
    - To load an individual time step, click the gray triangle beside the file name and select the desired time step.
- **ParaView** filter concept
  - Data in **ParaView** is treated like a stream. Data is loaded and can then "flow" into various filters to manipulate the data.

- Basic plotting
  - Field data on grid
    - Example of strain rates (`FEM_Grid_v-mesh.#####` -> StrainRateInvariantField)
      - Changing the contour color range
        - Click the icon with the two opposed green arrows and the letter "c" on it. Enter range.
      - Changing the color scheme
        - Click "Edit Color Map" button in toolbar, then click folder with heart icon in the Color Map Editor panel
  - Cloud particle data
    - Example of viscosity data
      - Changing the color scheme (again)
        - Same process as above
      - Using logrithmic color scaling
        - Tick "Use log scale when mapping data to colors" in Color Map Editor panel
  - Velocity vectors
    - Click on the glyphs icon in the toolbar and click Apply.
    - Scaling the velocity vectors
      - In Properties panel on the left, scroll down to the section called Scaling. Set the Scale Mode to "vector" and enter a scaling factor that produces reasonable vector lengths
    - Decimating velocity fields
      - In the Masking section, you can switch the Glyph Mode to "Every Nth Point" and set the Stride to a larger value
  - Contouring
    - Click on the Contour tool icon in the toolbar. Select the existing value in the list under Isosurfaces, click the minus icon and then click on the graduated line icon beneath to define the range and number of intervals.
  - Clipping
    - Can be done using the Clip tool in the toolbar (not covered)

- More advanced Plotting
  - Splitting windows
    - Windows can be split using the icons at the top right of the Layout panel
  - Linking cameras
    - After splitting a window, right-click on one of the panels, select "Link Camera..." and click on another panel to create the link. Both panels will now show the same view of the data.
  - Adding text/time step
    - Filters -> Temporal -> Annotate Time Filter
  - Using the calculator (not covered)
  - Adding axes to the plot/manipulating the axis labels
    - Scroll down to Cube Axes in the Properties panel on the left and tick Show Axis
  - Changing the velocity vector glyphs (not covered)
  - Translating/rotating velocity vectors or the plotted data (not covered)
  - Opacity, line widths/point sizes (not covered)

- Saving output
  - Screenshots
    - File -> Save Screenshot...
    - Changing the effective resolution
      - Generally, the resolution by default in ParaView looks crappy. When saving a screenshot, we suggest clicking on the Lock Aspect icon (red squares to right of resolution) and setting the first resolution number to at least 1600.
  - Animations
    - File -> Save Animation...
  - **ParaView** states (not covered)
