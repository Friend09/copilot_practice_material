# Vision for Copilot - Example Prompts

Use these prompts when uploading images to Copilot Chat.

## UI Component Generation

### Simple Button
```
Convert this button design to a React component.
Requirements:
- TypeScript
- Tailwind CSS for styling
- Support for disabled state
- Include hover and focus states
- Add proper ARIA attributes
```

### Input Field
```
Create a reusable input component from this design.
Include:
- Label and placeholder
- Error state styling
- Helper text support
- Icon support (left and right)
- TypeScript props interface
```

### Card Component
```
Generate a card component matching this design.
Features needed:
- Header, body, footer sections
- Optional image
- Customizable padding
- Shadow and border radius
- Responsive on mobile
```

## Complete Layouts

### Landing Page Hero
```
Convert this hero section to HTML/CSS/JS.
Specifications:
- Full viewport height
- Background image with overlay
- Centered content
- CTA button
- Responsive typography
- Mobile-optimized
```

### Dashboard Layout
```
Create a dashboard layout from this mockup.
Include:
- Responsive sidebar (collapsible on mobile)
- Top navigation bar
- Main content area with grid
- Card widgets
- Use CSS Grid and Flexbox
```

### Product Page
```
Implement this product page design.
Components:
- Image gallery with thumbnails
- Product details section
- Add to cart functionality
- Related products grid
- Reviews section
- Mobile-first responsive design
```

## Forms

### Login Form
```
Generate a login form from this design.
Requirements:
- Email and password fields
- Remember me checkbox
- Form validation (client-side)
- Error message display
- Loading state on submit
- Forgot password link
- Social login buttons
```

### Multi-Step Form
```
Create a multi-step form component.
Features:
- Progress indicator
- Form state management
- Validation per step
- Back/Next navigation
- Summary page
- Submit handler
```

## Navigation

### Header Navigation
```
Build a responsive header navigation.
Include:
- Logo
- Menu items (Desktop: horizontal, Mobile: hamburger)
- Search bar
- User profile dropdown
- Shopping cart icon with badge
- Sticky on scroll
```

### Sidebar Navigation
```
Create a sidebar navigation component.
Features:
- Collapsible sections
- Active state highlighting
- Icons for each item
- Nested menu items
- Smooth transitions
```

## Data Display

### Data Table
```
Generate a data table component from this design.
Capabilities:
- Sortable columns
- Search/filter
- Pagination
- Row selection
- Responsive (horizontal scroll on mobile)
- Loading skeleton
```

### Chart/Graph Widget
```
Create a chart widget matching this design.
Requirements:
- Integrate with Chart.js or Recharts
- Responsive sizing
- Legend
- Tooltip on hover
- Data labels
- Color scheme matching design
```

## Email Templates

### Marketing Email
```
Convert to HTML email template.
Specifications:
- Table-based layout for compatibility
- Inline CSS
- Alt text for all images
- CTA button
- Mobile-responsive
- Test with Gmail, Outlook, Apple Mail
```

### Transactional Email
```
Generate a transactional email template.
Include:
- Clean, simple layout
- Order/transaction details
- Clear call-to-action
- Footer with company info
- Unsubscribe link
- Mobile-optimized
```

## Advanced Prompts

### With Animation
```
Implement this component with animations.
Animations needed:
- Fade in on mount
- Hover scale effect
- Smooth state transitions
- Use Framer Motion
- Respect user's motion preferences
```

### With Dark Mode
```
Create this component with dark mode support.
Requirements:
- Light and dark color schemes
- System preference detection
- Manual toggle option
- Smooth transition between modes
- Tailwind dark mode utilities
```

### With Accessibility Focus
```
Generate an accessible version of this component.
Accessibility features:
- Semantic HTML
- ARIA labels and roles
- Keyboard navigation
- Screen reader support
- Focus management
- High contrast mode support
```

### Component Library Style
```
Create this as a library component.
Requirements:
- Highly configurable via props
- Composition pattern
- Compound components (if applicable)
- TypeScript generics (where needed)
- Comprehensive prop types
- JSDoc documentation
```

## Refinement Prompts

### After Initial Generation
```
Improve this component:
- Extract reusable parts
- Add loading states
- Improve error handling
- Optimize performance
- Add unit tests
```

### Styling Adjustments
```
Update the styling:
- Adjust spacing to match design system
- Fix alignment issues
- Improve responsive behavior
- Add transition effects
- Polish hover states
```

### Add Functionality
```
Enhance this component with:
- Form validation
- API integration
- State management
- Error boundary
- Loading skeleton
```

## Combining Multiple Images

### Responsive Views
```
[Upload 3 images: mobile, tablet, desktop views]

Create a responsive component that matches these breakpoints:
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

Ensure smooth transitions between breakpoints.
```

### Before/After Comparison
```
[Upload current and desired design]

Refactor this component from the current design to the new design.
Maintain existing functionality while updating the visual appearance.
```

### Style Variations
```
[Upload 2-3 variations]

Create a component that supports these style variants:
- Default
- Outlined
- Ghost
- Solid

All sharing the same base functionality.
```

## Tips for Better Results

### Be Specific About Technology
```
✅ "Use React 18 with TypeScript, styled-components, and React Query"
❌ "Use React"
```

### Provide Constraints
```
✅ "Maximum 400px width on mobile, 1200px on desktop"
❌ "Make it responsive"
```

### Mention Existing Patterns
```
✅ "Follow the same pattern as components/Button.tsx"
❌ "Make a button"
```

### Request Tests
```
✅ "Include Jest tests with React Testing Library"
❌ "Add tests"
```

### Specify Accessibility Level
```
✅ "WCAG 2.1 Level AA compliance, including keyboard navigation"
❌ "Make it accessible"
```
