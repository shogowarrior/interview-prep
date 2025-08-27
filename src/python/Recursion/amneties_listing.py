# Context/Prompt: 
# Listings on Airbnb usually represent a single bookable unit of inventory. For some listings such as hotels, there are many bookable units of inventory. For those, listings can be created at levels beyond bookable inventory (e.g., at the property level). These form a parent-child relationship where properties of the parent are ‘accessible’ by the children (e.g., if the building has a common swimming pool, all units also have access to the swimming pool).
# For the purposes of this exercise, assume there is a max depth of 3 for listing hierarchies (i.e., a listing can have a parent and a grandparent).

# Listing hierarchy representation:
# Consider a data structure that is a list of tuples which holds pairs of listing ids to denote (parent listing, child listing). e.g., [(1,5), (1,6), (3,4), (2,3)] → 1 and 2 are top-level parents.

# Listing property attributes representation:
# You also have map of listing_ids (int) to attributes (set) to denote what amenities are present in a listing (note how the parent listings contain more general shared amenities that the child listings can also access):
# example:
# Write a method in the language of your choice that will take two inputs (list of tuples and a map) and update the map so that the child listing inherits the attributes of the parent listings, showing the complete list of attributes each listing has. For example, listing 5 should have six attributes in total in the final map.


from collections import defaultdict

relationships = [(1, 5), (1, 6), (3, 4), (2, 3)]

amenities_dict = {
  1: {"bbq_area", "lobby", "swimming_pool"},
  2: {"ballroom"},
  3: {"elevator", "parking_garage"},
  4: {"wifi", "table"},
  5: {"toaster_oven", "kitchen", "toilet"},
  6: {"standing_desk", "hammock"}
}

def update_amenities(relationships, amenities_dict):

    listingParentMap = defaultdict(int)
    for relationship in relationships:
        listingParentMap[relationship[1]] = relationship[0]

    amenities_dict_updated = defaultdict(set)
    for listing in amenities_dict.keys():
        current_listing = listing
        while current_listing:
            amenities_dict_updated[listing].update(amenities_dict[current_listing])
            current_listing = listingParentMap[current_listing]

    for listing, amenities in amenities_dict_updated.items():
        print(f"Listing {listing} has amenities: {amenities}")
        
    return amenities_dict_updated

amenities_dict_updated = update_amenities(relationships, amenities_dict)

expected_amneties = {
    1: {'swimming_pool', 'bbq_area', 'lobby'},
    2: {'ballroom'},
    3: {'ballroom', 'parking_garage', 'elevator'},
    4: {'elevator', 'wifi', 'parking_garage', 'table', 'ballroom'},
    5: {'swimming_pool', 'bbq_area', 'lobby', 'kitchen', 'toilet', 'toaster_oven'},
    6: {'hammock', 'standing_desk', 'bbq_area', 'lobby', 'swimming_pool'}
}

assert amenities_dict_updated == expected_amneties, "The updated amenities do not match the expected output."
