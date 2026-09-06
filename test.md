**@Figma**

Create a professional, fully editable IEEE/Elsevier-style neural network architecture diagram titled **"EnhancedEmotionNet96 Architecture"** in the currently opened Figma Design file.

Use a white background and vector objects only (no raster images). Every element must remain editable.

### Layout

Create a vertical pipeline with a branch connection.

```
Input RGB Image (96×96×3)
        │
        ▼
Preprocessing
Conv3×3 + BatchNorm + ReLU
        │
        ▼
Residual Block 1
SE Attention
        │
        ▼
MaxPool 2×2
        │
        ▼
Residual Block 2
SE Attention
        │
        ▼
MaxPool 2×2
        │
        ▼
Residual Block 3
SE Attention
       ├────────────► Intermediate Feature Bridge
       │                 Conv3×3
       │                 BN
       │                 ReLU
       │                 Adaptive AvgPool (6×6)
       │                    |
       ▼                    |
MaxPool 2×2                 |
        │                   |
        ▼                   |
Residual Block 4            |
        |                   |
        ⬇-------------------↲
SE Attention
        │
        └───────────────┐
                        ▼
              Multi-Scale Feature Fusion
          Concatenate Deep + Bridge Features
                        │
                        ▼
                   Flatten (23040)
                        │
                        ▼
             Fully Connected Classifier

Linear 23040→512
BatchNorm
ReLU
Dropout

↓

Linear 512→256
BatchNorm
ReLU
Dropout

↓

Linear 256→7

↓

Softmax

↓

Emotion Prediction
```

### IMPORTANT CONNECTIONS

Create these arrows exactly:

1. Preprocessing → Residual Block 1
2. Residual Block 1 → MaxPool 1
3. MaxPool 1 → Residual Block 2
4. Residual Block 2 → MaxPool 2
5. MaxPool 2 → Residual Block 3
6. Residual Block 3 branches into:

   * MaxPool 3
   * Intermediate Feature Bridge
7. MaxPool 3 → Residual Block 4
8. Residual Block 4 → Multi-Scale Feature Fusion
9. Intermediate Feature Bridge → Multi-Scale Feature Fusion
10. Multi-Scale Feature Fusion → Flatten
11. Flatten → Fully Connected layers
12. Fully Connected → Softmax
13. Softmax → Emotion Prediction

### Color Scheme

Blue — Convolution / Preprocessing

Orange — Residual Blocks

Green — SE Attention

Purple — Intermediate Feature Bridge

Dark Violet — Multi-Scale Feature Fusion

Gray — MaxPool

Red — Fully Connected Layers

Dark Green — Emotion Prediction

### Styling

* Rounded rectangles (12 px)
* 2 px border
* Thick connector arrows
* Auto Layout
* Even spacing
* Inter font
* Clean academic appearance
* Fully editable vectors
* Suitable for IEEE/Elsevier publication

Do not simplify the architecture or change the routing. Preserve the exact branching described above.



# Rate limits & access

## Who can access the MCP server?

Access to the Figma MCP server depends on your Figma plan and seat type. Per-minute rate limits apply in addition to daily or monthly tool call limits.

<table id="rate-limits-tier-table" class="tier-table">
  <thead>
      <tr>
          <th>Seat</th>
          <th>Starter</th>
          <th>Professional</th>
          <th>Organization</th>
          <th>Enterprise</th>
      </tr>
  </thead>
  <tbody>
      <tr class="tier-group-1 tier-first-row">
          <td class="seat-col">View, Collab</td>
          <td rowspan="2">Up to 6/month</td>
          <td>Up to 6/month</td>
          <td>Up to 6/month</td>
          <td>Up to 6/month</td>
      </tr>
      <tr class="tier-group-1 tier-last-row">
          <td class="seat-col">Dev, Full</td>
          <td>Up to 200/day<br />10/min</td>
          <td>Up to 200/day<br />15/min</td>
          <td>Up to 600/day<br />20/min</td>
      </tr>
  </tbody>
</table>

Rate limits apply to Figma MCP server tools that read data from Figma. Some tools, such as those that write to Figma files, are exempt from the rate limits. Exempt tools include:

- `add_code_connect_map`
- `generate_figma_design`
- `whoami`

Figma reserves the right to change rate limits.

## What if I'm rate-limited?

If you're encountering rate limits with the Figma MCP server, you can increase your limits in certain scenarios by upgrading your seat or plan.

- If you're on a Starter plan (6 tool calls per month), upgrade to a Pro, Organization, or Enterprise plan. Ensure you have a Full or Dev seat on the new plan.

- If you have a View or Collab seat on an Organization or Enterprise plan (6 tool calls per month), upgrade to a Full or Dev seat.

- If you have a Full or Dev seat on an Organization plan (200 tool calls per day), upgrade to an Enterprise plan (600 tool calls per day).

Full and Dev seats on Enterprise plans get the least-limited usage, as described in [Who can access the MCP server?](#who-can-access-the-mcp-server)

## Which MCP clients are supported?

To use the MCP server, youâ€™ll need a code editor or application that supports MCP servers (for example, VS Code, Cursor, or Claude Code).

Only clients listed in the [Figma MCP Catalog](https://www.figma.com/mcp-catalog/) are able to connect to the Figma MCP Server. If youâ€™re a developer interested in connecting a new MCP client, you can [join the waitlist](https://form.asana.com/?k=kBG-ejRQTdY8x_H6a4vM3Q&d=10497086658021).

## Why am I getting permission errors?

You can only access Figma content that you already have permission to view or edit. If you get an error indicating that resources canâ€™t be accessed:

1. **Check the file link:** Make sure itâ€™s a valid Figma Design, FigJam, or Figma Make file.
2. **Verify your user:** Run the whoami tool to confirm the email used for authentication. It also tells you all the plans the user belongs to and their seat types in these plans.
3. **Confirm permissions:** Ensure the user belongs to the plan to which the file being accessed belongs to as well