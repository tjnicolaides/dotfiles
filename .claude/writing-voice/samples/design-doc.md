## Real Estate: Metropolis Property Browse: Floorplan Diagram Images (tech design excerpt)

Scope & Goals

As part of the N16 Metropolis / "Airbnb-Friendly Apartments" hero launch, the eng team is investigating the most efficient manner of meeting the design team's visual requirements for the floorplan images seen in the Property Detail Page's "Available Units" carousel component.

These images, which are provided by the properties via the PMS feed integrations, should ideally share a common aspect ratio, and if that's not possible, an acceptable minimum padding around the image subject matter. To achieve either of these appearances, the correct background color should be used: if an image shows a diagram against a light blue background, the aspect ratio correction or minimum padding should match that light blue color.

Alternatives Considered

### Provide ACC team with ability to modify and replace in A4RE Admin Tools

The ACC team, which is a group of full-time Airbnb employees dedicated to content management for the Metropolis launch (as well as other recent hero launches) would be responsible for reviewing each floorplan that appears in the feeds for properties to be onboarded into the "Airbnb-Friendly Apartments" browse experience.

In this workflow, ACC team members would:
- Assess each floorplan available for publication because a property makes it available in the feeds
- If the floorplan is discovered to have a diagram that does not meet the minimum aspect ratio, the team member downloads it
- The team member modifies the image using software like Adobe Photoshop to "correct" the appearance
- The team member uploads the modified photo to the floorplan in the admin tools, and marks it as the "active photo"

Risks and concerns associated with this workflow:
- Replacing an image from the feeds effectively "severs" the tie between up-to-date feed data and the Property Browse experience. If a property manager changes a diagram image for a floorplan upstream in the feeds, that change would be obscured by the selection made by the ACC team.
- This requires a great deal of operational overhead for N16 launch, and would require indefinite upkeep. There are scheduled to be 200 properties live by N16, with another 200 in 2023, and each property can contain dozens of unique floor plans. More floor plans can be published on an ongoing basis as existing tenants leave and units become available for marketing.
- Given that we would need a person in the middle, new floor plans would need to be deactivated when they first appear, making it more likely that a property could at times have no visible available units. Overall, this will lead to out of date availability and could cause friction for our partners downstream when a prospective resident reaches out.

### Programmatically apply padding as diagram images are uploaded

Today, floor plan diagram images that are detected in a property's PMS feed data are uploaded to S3/Vermeer by Partner Hub for use on Airbnb.com products. A modification could be made to the upload workflow (and a utility provided to "backfill" existing diagram images) to detect an image's "background color" and apply a uniform aspect ratio or minimum padding.

The following integrations were proposed to the Metropolis eng team by Aditya Punjani, with the caveat that the engineering effort and availability to create these integrations would not align with the existing launch / review timeline for the Property Browse experience.

#### Leverage Crayon service

The closest available internal service available to perform this work is called Crayon, and is unfortunately not currently owned or maintained by any engineering team at Airbnb. Crayon is for choosing the "dominant color" in an image, for the purposes of creating a unique loading state, or assisting with overlaying text on photos in a color-contrast friendly way.

In addition to the difficulty associated with integrating with an unmaintained service, it should also be noted that the "dominant color" is not always the same as the color to be used to do diagram padding. For example, if a floor plan has a transparent PNG diagram, does "transparent" count as the dominant color? If a diagram takes up an unusual amount of space in the area of the image, would the color of the diagram itself be chosen by mistake?

#### Leverage new 3rd party service integration

An integration with a 3rd party image modification service, such as Cloudinary, may make sense - but significant investigation is required to see if such a service meets our requirements. Once engineering starts, it's estimated that it would not be available for another 2 months.

In addition to the concerns listed above, both of these solutions also raise the following:
- Is either integration "intelligent" enough to know whether a diagram requires padding to begin with? If not, applying padding to images that are already padded adequately will result in an image that is difficult for guests to view, because the diagram itself has "shrunk"
- How much manual effort is involved in "backfilling" floor plan diagram images that have already been uploaded?

### Programmatically apply padding as diagram images are viewed

In this client-side solution, floor plan diagram images would continue to be uploaded and stored as they currently are today, and no backfill would be required. There would be no manual overhead by content managers, nor any risk of "severing" feed data to match visual requirements. Instead, the burden of padding would be shifted into the JavaScript layer of the Property Browse experience, where custom code would detect an image's first pixel color after it has loaded, and then apply a uniform padding via CSS in the surrounding container.

Risks associated with this:
- This approach is also not "content-aware" enough to know whether additional padding or aspect ratio is needed to apply to images. Applying padding to images that are already adequate will result in images that are difficult for guests to view.
- Shifting the burden to user's browsers is expensive and will hurt the performance of the page, which in turn will likely harm conversion rates.
- Shifting the burden to user's browsers is also failure-prone: unlike a server-side process that can be reviewed in bulk using admin tools or S3, significant smoke-testing across properties will be required to verify that this works.
