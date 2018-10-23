# save all the maps in the charts folder
output_path = 'charts/maps'

# counter for the for loop
i = 0

# list of years (which are the column names at the moment)
list_of_years = ['200807','200907','201007','201107','201207','201307','201407','201507','201607']

# set the min and max range for the choropleth map
vmin, vmax = 200, 1200

# start the for loop to create one map per year
for year in list_of_years:
    # create map
    fig = merged1.plot(column=year, cmap='Blues', figsize=(10, 10), linewidth=0.8, edgecolor='0.8', vmin=vmin,
                       vmax=vmax, legend=True)

    # remove axis of chart
    fig.axis('off')

    # add a title
    fig.set_title('Violent crimes in London', \
                  fontdict={'fontsize': '25',
                            'fontweight': '3'})

    # this will save the figure as a high-res png in the output path. you can also save as svg if you prefer.
    filepath = os.path.join(output_path, only_year + '_violence.jpg')
    chart = fig.get_figure()
    chart.savefig(filepath, dpi=300)

    # create an annotation for the year by grabbing the first 4 digits
    only_year = year[:4]

    # position the annotation to the bottom left
    fig.annotate(only_year,
                 xy=(0.1, .225), xycoords='figure fraction',
                 horizontalalignment='left', verticalalignment='top',
                 fontsize=35)