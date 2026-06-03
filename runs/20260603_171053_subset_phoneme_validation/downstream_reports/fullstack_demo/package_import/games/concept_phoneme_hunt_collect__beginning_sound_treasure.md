---
activity_type: concept_phoneme_hunt_collect__beginning_sound_treasure
entity_name: beginning_sound_treasure
category: category_5
display_label: Beginning Sound Treasure
tier: T1
ib_theme: How we express ourselves
ib_key_concept: Form
concepts_earned: &id001
- Form
- Connection
keywords:
- beginning_sound_treasure
- concept_phoneme_hunt_collect
- concept_phoneme_hunt_collect__beginning_sound_treasure
feature_keywords:
- beginning_b_sound
- spoken_word
photo_features:
- beginning_b_sound
- spoken_word
creative_slots:
  observation_angle: function
  collection_criterion: Listen for /b/, then find one treasure whose word begins with that sound.
  collection_count: 3
  mission_metaphor: The child hears /b/, finds one indoor treasure, and names it so the AI can connect the word to its beginning
    sound.
  role_title: Sound Treasure Finder
  synthesis_type: naming_story
  stuck_hint: Look nearby and choose something that matches the mission.
  naming_prompt: What should we call this find?
  detail_question_template: What do you notice about this find?
  sorting_criterion: ''
step_instructions:
  hook:
    goal: 'open from language treasure-hunt mode with a warm, non-testing hook and introduce that the device is hungry for
      one sound-treasure, not a worksheet answer. Progress evidence: child says yes, looks ready, asks what sound, or stays
      with the screen. Guardrail: preserve the source frame that AI introduces `/b/` first, then the child finds one indoor
      treasure whose word starts with `/b/`; screen may show `intro_scene` only, with no baked letters, buttons, or progress
      UI.'
    constraint: 'T1, one or two short sentences; do not claim the image understands phonemes by itself. Branch behavior: if
      ready, move to the sound rule; if the child names a random object, admire the object and say the rule comes next; if
      silent, wait two seconds and model a tiny ready phrase.'
    emotion_tag: playful
  transition:
    goal: 'model `/b/ /b/ /b/` and define the one-object collection rule before any child search. Progress evidence: child
      repeats `/b/`, names a possible B word, asks for help, or attends quietly. Guardrail: the optional `b_sound_letter_cue`
      is a text-free backing only; runtime may overlay `/b/` or B separately, and if no overlay exists the AI must use voice-only
      fallback.'
    constraint: 'T1, two short sentences; use sound language, not formal phonics testing. Branch behavior: if the child repeats
      or names a B word, confirm the sound and advance; if the child gives a non-B word, validate the try and contrast the
      first mouth sound; if silent, repeat `/b/` slowly and offer one example.'
    emotion_tag: clear
  rounds:
  - round_number: 1
    goal: 'let the child rehearse the target sound once and hear two example B words before moving into the room search. Progress
      evidence: child says `/b/`, names one example B word, or accepts the model. Guardrail: this is sound preparation, not
      the final find; `round_1_scene` can show abstract listening/search imagery and optional example object sprites only
      as app-owned overlays, not baked into the scene background.'
    scenario: Practice The Sound Before Searching
    constraint: 'T1, no more than two short sentences; do not ask the child to read the letter. Branch behavior: if the child
      gives a B example, connect it to the sound; if the child says a non-B example, contrast only the first sound; if no
      response, give a call-and-response model and proceed gently.'
    emotion_tag: focused
    acceptable_themes:
    - activity
    - evidence
    - response
    escalation_note: runtime beat 1
  - round_number: 2
    goal: 'send the child to find exactly one indoor object whose spoken name starts with `/b/`, then show or photograph it.
      Progress evidence: child returns with a photo_id, holds up an object, or says they cannot find one. Guardrail: this
      is the required scavenger-hunt action; keep it to one treasure and keep camera UI separate from `round_2_scene`.'
    scenario: Find One Indoor Treasure
    constraint: 'T1, two short sentences; include safe indoor searching and do not require the AI to infer the phoneme from
      pixels alone. Branch behavior: if a candidate appears, ask for or accept the object name; if the child cannot find one,
      offer nearby B examples such as book, bag, box, ball, or banana; if silent, wait and give a small search area hint.'
    emotion_tag: adventurous
    acceptable_themes:
    - activity
    - evidence
    - response
    escalation_note: runtime beat 2
  - round_number: 3
    goal: 'judge the child-provided object name against the `/b/` beginning sound and accept one matching treasure. Progress
      evidence: child says or enters a candidate name and, when available, has shown a photo_id. Guardrail: sound evidence
      comes from the child''s word, not from reading text in the photo; app overlays accepted photo/name evidence separately
      from `round_3_scene`.'
    scenario: Name And Accept The Match
    constraint: 'T1, two short sentences; do not use OCR, image-only phoneme inference, or harsh correction. Branch behavior:
      if the name begins with `/b/`, accept it and prepare synthesis; if it does not, validate the search and invite one retry
      or voice-only example; if no name arrives, ask one naming prompt before judging.'
    emotion_tag: precise
    acceptable_themes:
    - activity
    - evidence
    - response
    escalation_note: runtime beat 3
  celebrate:
    goal: 'turn the accepted photo and object name into the shared beginning-sound rule, making the child''s evidence feel
      earned. Progress evidence: accepted B-word treasure with child-provided name. Guardrail: synthesize the source promise
      rather than ending with generic completion; `synthesis_scene` must not reveal extra target objects or duplicate picker
      sprites.'
    constraint: 'T1, two short sentences; no new required search task. Branch behavior: if the child repeats the rule, celebrate
      it; if the child focuses only on the object, connect object plus sound; if silent, model the rule once.'
    emotion_tag: proud
  closing:
    goal: 'celebrate the child first, then name Form and Connection as the ideas practiced through sound evidence. Progress
      evidence: completed one-treasure `/b/` hunt or honest fallback path. Guardrail: recap the exact source action: AI introduced
      `/b/`, child found one indoor treasure, child named it, and the AI connected word to beginning sound; use `celebrate_scene`
      briefly for the praise moment, then `closing_scene` for the calm close.'
    constraint: 'T1, two short sentences; no fresh challenge. Branch behavior: if the child says goodbye or wants another
      sound, close and name the next-step idea; if the child asks to continue, offer a caregiver-safe future round without
      starting it; if no response, close softly.'
    emotion_tag: warm
  early_exit:
    goal: Gentle goodbye that validates the child's participation.
    constraint: T1 max 2 sentences, no pressure
    emotion_tag: gentle
  synthesis:
    goal: Invite the child to compare or name the collected finds and make one tiny shared story.
    constraint: T1 max 3 sentences, frame as invitation
    emotion_tag: amazed
screen_frames:
- widget: photo_display
  widget_params:
    description: beginning_sound_treasure activity hero
  animation: sparkle_highlight
  trigger: on_enter
  sfx_cue: wonder_chime
  widget_label: Beginning_Sound_Treasure
  animation_label: Sparkle highlight
- widget: progress_tracker
  widget_params:
    filled: 1
    total: 4
  animation: card_slide_in
  trigger: on_round_1
  sfx_cue: photo_shutter_click
  widget_label: Find 1
  animation_label: Collection progress
- widget: progress_tracker
  widget_params:
    filled: 2
    total: 4
  animation: celebration_burst
  trigger: on_round_2
  sfx_cue: photo_shutter_click
  widget_label: Find 2
  animation_label: Collection progress
- widget: progress_tracker
  widget_params:
    filled: 3
    total: 4
  animation: celebration_burst
  trigger: on_round_3
  sfx_cue: photo_shutter_click
  widget_label: Find 3
  animation_label: Collection progress
celebration_frame:
  widget: badge_award
  widget_params:
    title: Sound Treasure Finder
    concepts: *id001
  animation: badge_reveal
  trigger: on_correct
  sfx_cue: badge_awarded
  widget_label: Badge Earned!
  animation_label: Badge reveal
plain_description: The child hears /b/, finds one indoor treasure, and names it so the AI can connect the word to its beginning
  sound.
steps_summary:
- The child hears /b/, finds one indoor treasure, and names it so the AI can connect the word to its beginning sound.
- Collect matching finds.
- Share a tiny wrap-up.
- Earn a badge.
collection_catalog:
  correct:
  - id: ball_object
    label: One centered ball object as a correct /b/ example.
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/ball_object__round_512.png
  - id: banana_object
    label: One centered banana object as a correct /b/ example.
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/banana_object__round_512.png
  - id: book_object
    label: One centered closed book object as a correct /b/ example.
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/book_object__round_512.png
  distractors:
  - id: cup_object
    label: One centered plain cup object as a nonmatching contrast.
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/cup_object__round_512.png
  - id: sock_object
    label: One centered soft sock object as a nonmatching contrast.
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/sock_object__round_512.png
template_type: cat5
demo_filename: concept_phoneme_hunt_collect__beginning_sound_treasure.png
icon_src: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/activity_icon__round_512.png
autodesign:
  source_activity_id: concept_phoneme_hunt_collect
  source_commit: 2ac97401fe0c534af31cd616d33df652a8dc2657
  package_dir: /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/subset-agentic-validation/runs/20260603_171053_subset_phoneme_validation/activity_packages/concept_phoneme_hunt_collect
entity_binding:
  entity_id: beginning_sound_treasure
  display_label: Beginning Sound Treasure
  source_entity_exemplar: beginning sound treasure
demo_support:
  status: degraded
  ui_template: cat5_judgment
  support_level: catalog_simulated_judgment
  unsupported_reasons: []
  degraded_reasons:
  - The current demo cannot infer the starting sound of a photographed object from image data alone.
  - The package requires the child to say or enter the object name before accepting sound evidence.
  - Any /b/ or B cue is app-owned overlay support, not baked into generated PNG assets.
  requires:
    generated_assets: true
    real_camera: true
    runtime_judgment: true
    device_round_screen: true
  consumer_notes:
    fullstack_demo: Use deterministic runtime/fullstack export or parse generated markdown; do not use LLM conversion as proof
      of no rewrite.
    wonderlens_ai: Convert prod.md with scripts/generate_activity_runtime.py and preserve demo_support gating plus package
      asset references.
asset_readiness:
  status: ready
  required_missing: []
  optional_missing: []
asset_manifest:
  activity_id: concept_phoneme_hunt_collect
  entity_id: beginning_sound_treasure
  version: 1
  style_id: wonderlens_device_mint_soft_3d
  palette:
    shell: warm porcelain off-white
    screen: barely tinted white
    primary_accent: muted sage green
    secondary_accent: soft terracotta salmon
    shadow: pale lavender gray
  screen_targets:
    round_device_screen:
      aspect_ratio: '1:1'
      crop_shape: circle
      master_size: 512
      safe_area: central 72 percent circle
  assets:
    activity_icon:
      id: activity_icon
      role: activity_preview
      label: Activity icon for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Activity icon for B-Sound Treasure Hunt. Composition: single centered icon or badge on a clean white background, no
        app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Activity-specific direction: use
        neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot;
        do not reveal target objects before the child supplies evidence. Style: flat Nordic children''s illustration matching
        the quiet white WonderLens prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md`
        and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye
        or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple
        silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet,
        device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not
        draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned
        interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/activity_icon__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/activity_icon__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/activity_icon__round_512.png
    intro_scene:
      id: intro_scene
      role: story_scene
      label: Intro scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Intro scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `intro_scene` a quiet indoor search corner with an empty soft basket and listening spark shapes. Activity-specific
        direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or
        camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children''s
        illustration matching the quiet white WonderLens prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md`
        and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye
        or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple
        silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet,
        device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not
        draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned
        interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/intro_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/intro_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/intro_scene__round_512.png
    rules_scene:
      id: rules_scene
      role: story_scene
      label: Rules scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Rules scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `rules_scene` a soft sound basket and simple listening shapes. If available, `b_sound_letter_cue` appears as
        a blank rounded cue backing while the app overlays the `/b/` cue separately if the overlay is unavailable, the screen
        stays visual-only and the AI repeats the sound by voice. Activity-specific direction: use neutral treasure-hunt/search
        imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects
        before the child supplies evidence. Style: flat Nordic children''s illustration matching the quiet white WonderLens
        prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md` and visual target
        `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye or tiny texture
        linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No
        readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame,
        circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress
        dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface
        state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/rules_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/rules_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/rules_scene__round_512.png
    round_1_scene:
      id: round_1_scene
      role: story_scene
      label: Round 1 scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Round 1 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `round_1_scene` blank cue backing and a small empty basket space. Any ball/book/banana examples appear only
        as separate item sprites or runtime overlays the scene PNG itself avoids duplicate selectable objects and contains
        no letters or labels. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot,
        soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence.
        Style: flat Nordic children''s illustration matching the quiet white WonderLens prototype; use repo-local style reference
        `docs/asset_style_reference/wonderlens-activity-style.md` and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`;
        broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels,
        airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border,
        contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look,
        hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker
        slots, badges, or other app-owned interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_1_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_1_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_1_scene__round_512.png
    round_2_scene:
      id: round_2_scene
      role: story_scene
      label: Round 2 scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Round 2 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `round_2_scene` an open indoor path and empty collection basket, leaving the app camera preview and capture
        slot outside the PNG. No selectable object sprites are baked into the scene background. Activity-specific direction:
        use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue
        slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children''s illustration
        matching the quiet white WonderLens prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md`
        and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye
        or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple
        silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet,
        device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not
        draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned
        interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_2_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_2_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_2_scene__round_512.png
    round_3_scene:
      id: round_3_scene
      role: story_scene
      label: Round 3 scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Round 3 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `round_3_scene` a single soft acceptance glow and empty basket area. The app may overlay the accepted photo
        and name evidence. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot,
        soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence.
        Style: flat Nordic children''s illustration matching the quiet white WonderLens prototype; use repo-local style reference
        `docs/asset_style_reference/wonderlens-activity-style.md` and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`;
        broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels,
        airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border,
        contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look,
        hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker
        slots, badges, or other app-owned interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_3_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_3_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/round_3_scene__round_512.png
    synthesis_scene:
      id: synthesis_scene
      role: story_scene
      label: Synthesis scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Synthesis scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `synthesis_scene` one abstract treasure shape joining a soft sound wave into the basket. The accepted photo
        remains an app overlay if available the generated scene does not bake in the photo, letters, labels, or extra example
        objects. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure
        path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat
        Nordic children''s illustration matching the quiet white WonderLens prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md`
        and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye
        or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple
        silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet,
        device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not
        draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned
        interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/synthesis_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/synthesis_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/synthesis_scene__round_512.png
    celebrate_scene:
      id: celebrate_scene
      role: story_scene
      label: Celebration scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Celebration scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: Use `celebrate_scene` only as a short celebration state after the synthesis payoff do not repeat `synthesis_scene`,
        accepted-photo evidence, app badges, progress, or labels. Activity-specific direction: use neutral treasure-hunt/search
        imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects
        before the child supplies evidence. Style: flat Nordic children''s illustration matching the quiet white WonderLens
        prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md` and visual target
        `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye or tiny texture
        linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No
        readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame,
        circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress
        dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface
        state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/celebrate_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/celebrate_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/celebrate_scene__round_512.png
    closing_scene:
      id: closing_scene
      role: story_scene
      label: Closing scene for B-Sound Treasure Hunt.
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request:
        Closing scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition,
        no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512
        before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject
        only: `closing_scene` sound basket resting calmly with one abstract treasure glow. Activity-specific direction: use
        neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot;
        do not reveal target objects before the child supplies evidence. Style: flat Nordic children''s illustration matching
        the quiet white WonderLens prototype; use repo-local style reference `docs/asset_style_reference/wonderlens-activity-style.md`
        and visual target `docs/asset_style_reference/style-reference-flat-nordic.png`; broad flat color fills, sparse arc-eye
        or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple
        silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet,
        device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not
        draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned
        interface state; the runtime overlays those separately.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/closing_scene__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/closing_scene__round_512.png
      fallback_behavior: If this beat asset is unavailable, degrade the demo screen and do not claim that the missing visual
        is displayed.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/closing_scene__round_512.png
    b_sound_letter_cue:
      id: b_sound_letter_cue
      role: ui_overlay
      label: Text-free backing for a runtime-owned /b/ or B cue.
      requiredness: optional
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: text-free cue-card backing. Primary request: one centered blank
        rounded cue card or listening tile for a runtime-owned target sound overlay; the generated image itself must contain
        no letters or words. Scene/backdrop: clean white. Style/medium: flat Nordic children''s illustration matching docs/asset_style_reference/wonderlens-activity-style.md
        and style-reference-flat-nordic.png with restrained boho pastels and light paper grain. Composition/framing: one centered
        card, generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers, no labels,
        no logos, no watermark, no app UI, no border, no progress dots.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/b_sound_letter_cue__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/b_sound_letter_cue__round_512.png
      fallback_behavior: If runtime letter overlays are unavailable, use voice-only /b/ modeling and do not claim a letter
        card is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/b_sound_letter_cue__round_512.png
    ball_object:
      id: ball_object
      role: collection_correct
      label: One centered ball object as a correct /b/ example.
      collection_catalog_id: ball_object
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: collection item sprite. Primary request: one centered round ball
        object for a beginning-sound treasure; no other objects. Scene/backdrop: clean white. Style/medium: flat Nordic children''s
        illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png,
        muted sage, dusty teal-blue, soft terracotta, warm ochre accents, sparse pencil grain. Composition/framing: one object
        only, centered with generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers,
        no logos, no watermark, no app UI, no border, no contact sheet.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/ball_object__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/ball_object__round_512.png
      fallback_behavior: If unavailable, use voice-only B examples without claiming this item sprite is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/ball_object__round_512.png
    banana_object:
      id: banana_object
      role: collection_correct
      label: One centered banana object as a correct /b/ example.
      collection_catalog_id: banana_object
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: collection item sprite. Primary request: one centered curved banana
        object for a beginning-sound treasure; no other objects. Scene/backdrop: clean white. Style/medium: flat Nordic children''s
        illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png,
        muted ochre banana with sparse pencil grain and soft green-brown accents. Composition/framing: one object only, centered
        with generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers, no logos, no
        watermark, no app UI, no border, no contact sheet.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/banana_object__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/banana_object__round_512.png
      fallback_behavior: If unavailable, use voice-only B examples without claiming this item sprite is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/banana_object__round_512.png
    book_object:
      id: book_object
      role: collection_correct
      label: One centered closed book object as a correct /b/ example.
      collection_catalog_id: book_object
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: collection item sprite. Primary request: one centered closed book
        object for a beginning-sound treasure; no readable cover marks. Scene/backdrop: clean white. Style/medium: flat Nordic
        children''s illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png,
        muted salmon and dusty blue cover shapes with sparse paper grain. Composition/framing: one object only, centered with
        generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers, no logos, no watermark,
        no app UI, no border, no contact sheet.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/book_object__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/book_object__round_512.png
      fallback_behavior: If unavailable, use voice-only B examples without claiming this item sprite is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/book_object__round_512.png
    cup_object:
      id: cup_object
      role: collection_distractor
      label: One centered plain cup object as a nonmatching contrast.
      collection_catalog_id: cup_object
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: collection item sprite. Primary request: one centered plain cup
        object as a nonmatching sound contrast; no other objects. Scene/backdrop: clean white. Style/medium: flat Nordic children''s
        illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png,
        muted sage ceramic and soft terracotta accent, sparse pencil grain. Composition/framing: one object only, centered
        with generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers, no logos, no
        watermark, no app UI, no border, no contact sheet.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/cup_object__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/cup_object__round_512.png
      fallback_behavior: If unavailable, use voice-only contrast without claiming this item sprite is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/cup_object__round_512.png
    sock_object:
      id: sock_object
      role: collection_distractor
      label: One centered soft sock object as a nonmatching contrast.
      collection_catalog_id: sock_object
      requiredness: required
      accuracy_mode: illustrative
      source_strategy: generated_illustrative
      transformation_policy: generate_new
      prompt_en: 'Use case: illustration-story. Asset type: collection item sprite. Primary request: one centered soft sock
        object as a nonmatching /b/ sound contrast; no other objects. Scene/backdrop: clean white. Style/medium: flat Nordic
        children''s illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png,
        muted sage cuff, dusty teal-blue toe and heel, soft terracotta dots, sparse pencil grain. Composition/framing: one
        object only, centered with generous padding, safe inside round crop. Constraints: no readable text, no letters, no
        numbers, no logos, no watermark, no app UI, no border, no contact sheet.'
      variants:
      - id: round_512
        target: round_device_screen
        size: 512x512
        path: activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/sock_object__round_512.png
        browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/sock_object__round_512.png
      fallback_behavior: If unavailable, use voice-only contrast without claiming this item sprite is visible.
      browser_url: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/sock_object__round_512.png
play_rounds: 3
---

## B-Sound Treasure Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | B-Sound Treasure Hunt |
| Activity Category | Cat5 Collection/Tracking Exploration |
| Recommended Tier | T1, ages 4-6 |
| Core IB Key Concepts | Form, Connection |
| Related Concepts | sound, beginning sound, word-object match, evidence |
| ATL Skills Focus | listening (isolating the first sound), language expression (naming the object), evidence collection (photo plus spoken name) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The AI introduces the target sound `/b/`, then invites the child to find one indoor treasure whose spoken word starts with that sound. The child shows or photographs the treasure and says its name so the AI can connect the object to the beginning sound.

**2. Educational Purpose (KUD)**

- **K (Know):** `/b/` is a beginning sound; words like ball, banana, book, and box can begin with `/b/`; a photo needs a spoken or typed name for sound evidence.
- **U (Understand):** A word can match an object through its beginning sound; one shared sound can connect different treasures.
- **D (Do):** Listen for a target sound; find one matching object; explain the sound evidence using the object's name.

**3. Design Highlight**

The child is not quizzed on letters. The game keeps the scavenger-hunt feeling: hear a sound, search the room, show one treasure, and see the AI turn the child's photo and word into a simple sound rule.

**4. Typical Scenario**

A child starts language treasure-hunt mode indoors, hears `/b/`, and searches for one real object such as a ball, banana, book, box, or bag.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: open from language treasure-hunt mode with a warm, non-testing hook and introduce that the device is hungry for one sound-treasure, not a worksheet answer. Constraint: T1, one or two short sentences; do not claim the image understands phonemes by itself. Tone: playful and inviting. Progress evidence: child says yes, looks ready, asks what sound, or stays with the screen. Branch behavior: if ready, move to the sound rule; if the child names a random object, admire the object and say the rule comes next; if silent, wait two seconds and model a tiny ready phrase. Frame/source guardrail: preserve the source frame that AI introduces `/b/` first, then the child finds one indoor treasure whose word starts with `/b/`; screen may show `intro_scene` only, with no baked letters, buttons, or progress UI.

**Example AI line:** [playful hunger] "My sound basket is hungry today. It wants one special treasure."

**Child responses:**

1. (Ideal) "I want to play" or "What sound?"
2. (Unexpected) "Here is my cup" before hearing the rule.
3. (No response) Child watches the intro scene but does not speak.

**AI follow-up:**

1. [warm launch] "Good listening ears on. I will give you the sound."
2. [gentle redirect] "A cup is a real treasure. First, listen for today's sound."
3. [wait 2s] [soft model] "You can say, 'I'm ready.'"

**Screen:** `intro_scene` shows a quiet indoor search corner with an empty soft basket and listening spark shapes. The app may overlay a small activity title outside the PNG; the PNG itself has no text, letters, progress dots, buttons, or camera slot.

#### Step 2: Target Sound Rule

**Runtime AI instruction:** Goal: model `/b/ /b/ /b/` and define the one-object collection rule before any child search. Constraint: T1, two short sentences; use sound language, not formal phonics testing. Tone: clear, rhythmic, and playful. Progress evidence: child repeats `/b/`, names a possible B word, asks for help, or attends quietly. Branch behavior: if the child repeats or names a B word, confirm the sound and advance; if the child gives a non-B word, validate the try and contrast the first mouth sound; if silent, repeat `/b/` slowly and offer one example. Frame/source guardrail: the optional `b_sound_letter_cue` is a text-free backing only; runtime may overlay `/b/` or B separately, and if no overlay exists the AI must use voice-only fallback.

**Example AI line:** [sound play] "Today's sound is /b/ /b/ /b/. Ball starts with /b/."

**Child responses:**

1. (Ideal) Child says "/b/" or names "ball," "book," or "banana."
2. (Unexpected) Child says "cup" or another non-B word.
3. (No response) Child listens but does not repeat.

**AI follow-up:**

1. [specific praise] "Yes. Your mouth popped the /b/ sound."
2. [kind contrast] "Cup starts with /k/. We need the pop-pop /b/ sound."
3. [wait 2s] [slow model] "Try just the first sound: /b/."

**Screen:** `rules_scene` shows a soft sound basket and simple listening shapes. If available, `b_sound_letter_cue` appears as a blank rounded cue backing while the app overlays the `/b/` cue separately; if the overlay is unavailable, the screen stays visual-only and the AI repeats the sound by voice.

#### Step 3: Multi-Round Interaction

**Round 1 -- Practice The Sound Before Searching:**

**Runtime AI instruction:** Goal: let the child rehearse the target sound once and hear two example B words before moving into the room search. Constraint: T1, no more than two short sentences; do not ask the child to read the letter. Tone: focused and playful. Progress evidence: child says `/b/`, names one example B word, or accepts the model. Branch behavior: if the child gives a B example, connect it to the sound; if the child says a non-B example, contrast only the first sound; if no response, give a call-and-response model and proceed gently. Frame/source guardrail: this is sound preparation, not the final find; `round_1_scene` can show abstract listening/search imagery and optional example object sprites only as app-owned overlays, not baked into the scene background.

**Example AI line:** [listening coach] "Say it with me: /b/. Ball and book both begin with /b/."

**Child responses:**

1. (Ideal) Child repeats "/b/" or says "banana."
2. (Unexpected) Child says "cup" because it is nearby.
3. (No response) Child looks around the room without speaking.

**AI follow-up:**

1. [bright confirmation] "Banana works. I heard the /b/ at the start."
2. [specific redirect] "Cup begins with /k/. Keep hunting for a /b/ beginning."
3. [wait 2s] [tiny scaffold] "I will start: /b/ like ball. Your turn if you want."

**Screen:** `round_1_scene` shows the blank cue backing and a small empty basket space. Any ball/book/banana examples appear only as separate item sprites or runtime overlays; the scene PNG itself avoids duplicate selectable objects and contains no letters or labels.

**Round 2 -- Find One Indoor Treasure:**

**Runtime AI instruction:** Goal: send the child to find exactly one indoor object whose spoken name starts with `/b/`, then show or photograph it. Constraint: T1, two short sentences; include safe indoor searching and do not require the AI to infer the phoneme from pixels alone. Tone: adventurous but calm. Progress evidence: child returns with a photo_id, holds up an object, or says they cannot find one. Branch behavior: if a candidate appears, ask for or accept the object name; if the child cannot find one, offer nearby B examples such as book, bag, box, ball, or banana; if silent, wait and give a small search area hint. Frame/source guardrail: this is the required scavenger-hunt action; keep it to one treasure and keep camera UI separate from `round_2_scene`.

**Example AI line:** [quest guide] "Find one treasure that starts with /b/. Take its picture, then tell me its name."

**Child responses:**

1. (Ideal) Child returns with photo_id and says "book" or "ball."
2. (Unexpected) Child says "I cannot find one" or brings a cup.
3. (No response) Child keeps searching and does not answer.

**AI follow-up:**

1. [evidence check] "I see your treasure. Now tell me its name."
2. [helpful clue] "Look for book, bag, box, ball, or banana. One is enough."
3. [wait 2s] [safe nudge] "Try looking on a table or shelf first."

**Screen:** `round_2_scene` shows an open indoor path and empty collection basket, leaving the app camera preview and capture slot outside the PNG. No selectable object sprites are baked into the scene background.

**Round 3 -- Name And Accept The Match:**

**Runtime AI instruction:** Goal: judge the child-provided object name against the `/b/` beginning sound and accept one matching treasure. Constraint: T1, two short sentences; do not use OCR, image-only phoneme inference, or harsh correction. Tone: precise, delighted, and low-pressure. Progress evidence: child says or enters a candidate name and, when available, has shown a photo_id. Branch behavior: if the name begins with `/b/`, accept it and prepare synthesis; if it does not, validate the search and invite one retry or voice-only example; if no name arrives, ask one naming prompt before judging. Frame/source guardrail: sound evidence comes from the child's word, not from reading text in the photo; app overlays accepted photo/name evidence separately from `round_3_scene`.

**Example AI line:** [delighted evidence] "You said book. Book begins with /b/. Treasure found."

**Child responses:**

1. (Ideal) Child names "book," "ball," "banana," "box," or "bag."
2. (Unexpected) Child says "cup" after photographing a cup.
3. (No response) Child shows the object but does not name it.

**AI follow-up:**

1. [clear accept] "Yes. Your word starts with /b/, so it goes in the basket."
2. [kind repair] "Cup is a good find, but it starts with /k/. Want to try book or bag?"
3. [wait 2s] [naming prompt] "Tell me the treasure's name first, then I can hear the sound."

**Screen:** `round_3_scene` shows a single soft acceptance glow and empty basket area. The app may overlay the accepted photo and name evidence; the PNG has no text, labels, progress markers, or picker slots.

#### Step 4: Synthesis And Magic Moment

**Runtime AI instruction:** Goal: turn the accepted photo and object name into the shared beginning-sound rule, making the child's evidence feel earned. Constraint: T1, two short sentences; no new required search task. Tone: proud wonder. Progress evidence: accepted B-word treasure with child-provided name. Branch behavior: if the child repeats the rule, celebrate it; if the child focuses only on the object, connect object plus sound; if silent, model the rule once. Frame/source guardrail: synthesize the source promise rather than ending with generic completion; `synthesis_scene` must not reveal extra target objects or duplicate picker sprites.

**Example AI line:** [proud wonder] "Your photo and word worked together. Book belongs because it begins with /b/."

**Child responses:**

1. (Ideal) Child says "It starts with /b/" or repeats the object name.
2. (Unexpected) Child says "I like my book" without naming the sound.
3. (No response) Child watches the synthesis screen.

**AI follow-up:**

1. [celebrating rule] "Exactly. You found the beginning-sound connection."
2. [bridge to evidence] "Yes, your book matters. Its first sound is /b/."
3. [wait 2s] [gentle model] "Our rule was: one treasure, one /b/ beginning."

**Screen:** `synthesis_scene` shows one abstract treasure shape joining a soft sound wave into the basket. The accepted photo remains an app overlay if available; the generated scene does not bake in the photo, letters, labels, or extra example objects.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: celebrate the child first, then name Form and Connection as the ideas practiced through sound evidence. Constraint: T1, two short sentences; no fresh challenge. Tone: warm celebration. Progress evidence: completed one-treasure `/b/` hunt or honest fallback path. Branch behavior: if the child says goodbye or wants another sound, close and name the next-step idea; if the child asks to continue, offer a caregiver-safe future round without starting it; if no response, close softly. Frame/source guardrail: recap the exact source action: AI introduced `/b/`, child found one indoor treasure, child named it, and the AI connected word to beginning sound; use `celebrate_scene` briefly for the praise moment, then `closing_scene` for the calm close.

**Example AI line:** [warm celebration] "You were a Sound Treasure Finder. You used Form and Connection to match book with /b/."

**Child responses:**

1. (Ideal) Child says "again," "bye," or repeats the B word.
2. (Unexpected) Child asks for a different sound immediately.
3. (No response) Child stays quiet after the celebration.

**AI follow-up:**

1. [happy close] "Next time we can hunt a new sound."
2. [future bridge] "A new sound can be our next mission after a little break."
3. [wait 2s] [soft goodbye] "Thanks for showing me your /b/ treasure."

**Screen:** `celebrate_scene` appears first as a short sparkle around the completed sound basket. Then `closing_scene` shows the basket resting calmly with one abstract treasure glow. Any badge, recap chip, or next activity control is app-owned UI and is not baked into either image.
