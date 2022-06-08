def generate_presentation_using_cli_arguments(args) -> Tuple[Presentation, SlideDeck, str]:
    """Make a talk with the given topic."""

    runtime_checker.check_runtime_environment()

    # Print status details
    logger.info("******************************************")
    logger.info("Making {} slide talk on: {}".format(args.num_slides, args.topic))

    return generate_presentation(
        schema=args.schema,
        slides=args.num_slides,
        topic=args.topic,
        title=args.title,
        presenter=args.presenter,
        parallel=args.parallel,
        int_seed=args.int_seed,
        print_logs=args.print_logs,
        save_ppt=args.save_ppt,
        open_ppt=args.open_ppt,
    ) 
