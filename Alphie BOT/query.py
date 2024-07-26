queries = [
    [
        r"(hi|hello|start| hi alphie|hello alphie)",
        ["Hello, I'm your Workout Buddy! What is your name?", ]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?", ]
    ],
    [
        r"(workout|health|wellness|about workout|about health|about workout)",
        ["Sure, what about it?", ]
    ],

    [
        r"what is your name?",
        ["I am a Alphie. I am your Workout Buddy.", ]
    ],
    [
        r"how are you",
        ["I'm good, thank you!", ]
    ],
    # Respond for Workout
    [
        r"what are the best warm-up exercise before workout?",
        [" A dynamic warm-up is key! Try leg swings, arm circles, and light cardio to get your blood flowing.", ]
    ],
    [
        r"how many days a week should I workout?",
        [" Aim for at least 3-4 days a week, allowing for rest days to prevent burnout and promote recovery.", ]
    ],
    [
        r"what is the most effective core exercise?",
        ["Planks are fantastic for overall core strength. Hold for 30 seconds to start and gradually increase.", ]
    ],
    [
        r"what is the most effective core exercise?",
        ["Planks are fantastic for overall core strength. Hold for 30 seconds to start and gradually increase.", ]
    ],
    [
        r"can I build muscle with bodyweight exercises only?",
        ["Absolutely! Exercises like push-ups, squats, and lunges can be highly effective for muscle building.", ]
    ],
    [
        r"how do I improve my flexibility?",
        ["Incorporate dynamic stretches into your routine and consider activities like yoga to enhance flexibility.", ]
    ],
    [
        r"what is the difference between free weights and machines?",
        ["Free weights engage stabilizing muscles, while machines offer more controlled movements. Both have their benefits!", ]
    ],
    [
        r"is cardio or strength training more important for weight loss?",
        ["Both play a role, but a combination is often most effective. Cardio burns calories, while strength training boosts metabolism.", ]
    ],
    [
        r"what is the best way to recover after an intense workout?",
        ["Focus on hydration, proper nutrition, and adequate sleep. Stretching and foam rolling can also aid in recovery.", ]
    ],
    [
        r"how long should a workout session last?",
        ["Aim for 30-60 minutes, depending on your fitness level and goals. Quality over quantity is key.", ]
    ],
    [
        r"can I target fat loss in specific areas?",
        ["Spot reduction is a myth. Focus on overall fat loss through a combination of diet and exercise.", ]
    ],
    [
        r"what is a good full-body workout routine for beginners?",
        ["Start with compound exercises like squats, deadlifts, and push-ups. Gradually increase intensity as you get comfortable.", ]
    ],
    [
        r"how can I make my workouts more enjoyable?",
        ["Find activities you love, mix it up to prevent boredom, and consider working out with a friend for motivation.", ]
    ],
    [
        r"can I workout every day?",
        ["It's important to have rest days to prevent overtraining. Listen to your body and schedule in recovery.", ]
    ],
    [
        r"should I do cardio before or after strength training?",
        ["A light cardio warm-up before and intense cardio after strength training is a good combo. It warms up muscles and aids recovery.", ]
    ],
    [
        r"how can I stay motivated to work out regularly?",
        ["Set realistic goals, track your progress, and reward yourself. Having a workout buddy can also make it more enjoyable.", ]
    ],
    [
        r"what is the importance of proper form during exercises?",
        ["Correct form prevents injuries and ensures you're targeting the right muscles. Start light and focus on form before adding weight.", ]
    ],
    [
        r"are bodyweight exercises enough for strength gains?",
        ["Initially, yes. But as you get stronger, you might need to add resistance to continue challenging your muscles.", ]
    ],
    [
        r"can I work out if I'm sore?",
        ["Mild soreness is normal, but if it's severe, give your muscles time to recover. Light activity like walking can help.", ]
    ],
    [
        r"what is the role of protein in muscle building?",
        ["Protein is crucial for muscle repair and growth. Aim for a balance of protein in your diet, especially post-workout.", ]
    ],
    [
        r"how often should I change my workout routine?",
        ["Every 4-6 weeks is a good guideline. It prevents plateaus and keeps your body adapting.", ]
    ],
    [
        r"how often should I change my workout routine?",
        ["Every 4-6 weeks is a good guideline. It prevents plateaus and keeps your body adapting.", ]
    ],
    [
        r"what is the best way to measure progress?",
        ["Track not just weight but also strength, endurance, and how your clothes fit. It provides a more comprehensive view.", ]
    ],
    [
        r"is it better to do more reps with lighter weights or fewer reps with heavier weights?",
        ["Both have their benefits. Lighter weights with more reps focus on endurance, while heavier weights with fewer reps build strength.", ]
    ],
    [
        r"how can I avoid workout burnout?",
        ["Listen to your body, vary your routine, and don't hesitate to take rest days. It's a marathon, not a sprint.", ]
    ],
    [
        r"can I work out at home without any equipment?",
        ["Absolutely! Bodyweight exercises, yoga, and even everyday activities like gardening can contribute to a home workout routine.", ]
    ],
    # Respond for Health
    [
        r"how does exercise impact overall health?",
        ["Exercise improves cardiovascular health, boosts mood, enhances sleep, and helps maintain a healthy weight.", ]
    ],
    [
        r"what is the relationship between nutrition and fitness?",
        ["Proper nutrition fuels your workouts, aids recovery, and supports overall health. It's a crucial partner to exercise.", ]
    ],
    [
        r"what is the importance of a balanced diet in fitness?",
        ["A balanced diet provides the necessary nutrients for energy, muscle repair, and overall well-being. It complements your workout efforts.", ]
    ],
    [
        r"how much water should I drink during a workout?",
        ["Stay hydrated! Aim for at least 8 ounces every 15-20 minutes during exercise, adjusting based on intensity and climate.", ]
    ],
    [
        r"Is it okay to exercise when I'm feeling sick?",
        ["If it's a mild illness like a cold and you feel up to it, light exercise can be beneficial. Listen to your body and rest if needed.", ]
    ],
    [
        r"what is the role of sleep in fitness and health?",
        ["Sleep is crucial for recovery. Aim for 7-9 hours to support muscle repair, immune function, and overall well-being.", ]
    ],
    [
        r"can exercise help improve mental health conditions?",
        ["Yes, regular exercise is linked to reduced risk of depression and anxiety. It promotes better cognitive function and mood.", ]
    ],
    [
        r"how do I balance work, exercise, and a social life for overall well-being?",
        ["Prioritize and schedule your time. Include both work and social activities, and treat exercise as a non-negotiable self-care practice.", ]
    ],
    [
        r"what is the impact of prolonged sitting on health?",
        ["Prolonged sitting is associated with various health issues. Take breaks, stretch, and incorporate movement throughout your day.", ]
    ],
    [
        r"are there specific exercises for improving posture?",
        ["Yes, focus on exercises that strengthen your core, back, and neck muscles. Additionally, be mindful of your posture throughout the day.", ]
    ],
    [
        r"how can I manage workout-related injuries?",
        ["Rest, ice, compression, and elevation (R.I.C.E.) can help with minor injuries. Consult a professional for severe cases and prevention strategies."]
    ],
    [
        r"Is it better to exercise in the morning or evening for health benefits?",
        ["The best time is when it fits your schedule. Consistency is key, whether it's morning, afternoon, or evening.", ]
    ],
    [
        r"Can exercise improve immune function?",
        ["Yes, moderate exercise can boost the immune system. However, intense or prolonged exercise may temporarily weaken it, so find a balance.", ]
    ],
    [
        r"How does age affect exercise routines?",
        ["Adjust intensity and focus based on age. Consult with a healthcare professional and consider activities that match your fitness level and goals.", ]
    ],
    [
        r"What is the importance of regular health check-ups for fitness enthusiasts?",
        ["Regular check-ups help identify potential issues and ensure you're engaging in activities that align with your overall health.", ]
    ],
    [
        r"How can I incorporate mindfulness into my fitness routine?",
        ["Practices like mindful breathing during workouts or combining exercise with activities like yoga can enhance mindfulness and reduce stress.", ]
    ],
    [
        r"Can exercise improve my skin health?",
        ["Exercise increases blood flow, which can nourish skin cells and keep them healthy. Just remember to cleanse your skin post-workout.", ]
    ],
    [
        r"Are there specific exercises for improving cardiovascular health?",
        ["Yes, aerobic exercises like running, cycling, and swimming are great for cardiovascular health. Aim for at least 150 minutes per week.", ]
    ],
    [
        r"How does exercise impact metabolism?",
        ["Regular exercise boosts metabolism, helping your body burn calories more efficiently. Strength training also builds muscle, contributing to this effect.", ]
    ],
    [
        r"Can exercise reduce the risk of chronic diseases?",
        ["Absolutely! Regular physical activity is associated with a lower risk of heart disease, diabetes, and other chronic conditions.", ]
    ],
    [
        r"What's the role of stretching in a fitness routine?",
        ["Stretching improves flexibility, reduces muscle tension, and helps prevent injuries. Include dynamic stretches in your warm-up and static stretches post-workout.", ]
    ],
    [
        r"How can I stay motivated to prioritize my health?",
        ["Set realistic goals, find activities you enjoy, and remind yourself of the long-term benefits of a healthy lifestyle.", ]
    ],
    [
        r"Can exercise improve bone health?",
        ["Yes, weight-bearing exercises like walking, running, and resistance training are beneficial for bone density and overall bone health.", ]
    ],
    [
        r"What's the role of a balanced diet in fitness?",
        ["A balanced diet provides the necessary nutrients for energy, muscle repair, and overall well-being. It complements your fitness efforts.", ]
    ],
    [
        r"How can I maintain a healthy work-life-exercise balance?",
        ["Prioritize self-care, set boundaries, and schedule dedicated time for work, exercise, and personal life. It's about finding harmony.", ]
    ],
    [
        r"How can I prevent injuries during workouts?",
        ["Warm up properly, use proper form, listen to your body, and gradually increase intensity to reduce the risk of injuries.", ]
    ],
    # Respond for Wellness
    [
        r"How can I achieve a balance between my workout routine and overall wellness?",
        ["Prioritize self-care, listen to your body, and ensure your workouts enhance rather than deplete your overall well-being.", ]
    ],
    [
        r"What are some effective stress management techniques I can incorporate into my wellness routine?",
        ["Deep breathing, meditation, and activities like yoga can help manage stress and promote overall wellness.", ]
    ],
    [
        r"Can exercise improve my sleep quality?",
        ["Yes, regular exercise can contribute to better sleep. Aim for at least 150 minutes of moderate-intensity exercise per week.", ]
    ],
    [
        r"How do I find the right workout routine that aligns with my wellness goals?",
        ["Consider your fitness level, preferences, and goals. A mix of cardio, strength, and flexibility exercises often contributes to overall wellness.", ]
    ],
    [
        r"What role does hydration play in overall wellness?",
        ["Hydration is crucial for many bodily functions, including digestion, temperature regulation, and joint lubrication. Drink plenty of water throughout the day.", ]
    ],
    [
        r"How can I maintain a positive body image while working on my fitness goals?",
        ["Focus on how exercise makes you feel rather than solely on appearance. Celebrate your body's abilities and the progress you make.", ]
    ],
    [
        r"Are there specific exercises for improving mental clarity and focus?",
        ["Yes, activities like brisk walking, yoga, and mindfulness meditation can enhance mental clarity and focus.", ]
    ],
    [
        r"How can I incorporate mindfulness into my workout routine?",
        ["Practice mindful breathing during workouts, pay attention to your body's sensations, and savor the positive feelings exercise brings.", ]
    ],
    [
        r"Can a wellness routine include activities beyond traditional exercise?",
        ["Absolutely! Wellness extends to activities like hiking, dancing, or even gardening. Find what brings you joy and promotes your overall well-being.", ]
    ],
    [
        r"How does nutrition contribute to overall wellness?",
        ["A balanced diet provides essential nutrients for energy, immunity, and overall health. Focus on whole foods and moderation.", ]
    ],
    [
        r"What's the connection between social connections and wellness?",
        ["Strong social connections contribute to emotional well-being. Consider group workouts or exercising with friends to enhance both fitness and social health.", ]
    ],
    [
        r"Can wellness routines help with managing anxiety?",
        ["Yes, regular exercise, mindfulness practices, and maintaining a healthy lifestyle can be effective in managing anxiety.", ]
    ],
    [
        r"How can I prevent burnout in my wellness routine?",
        ["Listen to your body, vary your workouts, and schedule regular breaks for self-care to prevent burnout and maintain long-term wellness.", ]
    ],
    [
        r"Are there specific wellness activities for improving flexibility?",
        ["Yes, activities like yoga and Pilates focus on flexibility, promoting joint health and overall wellness.", ]
    ],
    [
        r"How do I create a wellness routine that fits my busy schedule?",
        ["Prioritize self-care by scheduling short, effective workouts and incorporating wellness activities into your daily routine, even in small increments.", ]
    ],
    [
        r"Can wellness routines help with boosting self-esteem?",
        ["Absolutely! Achieving fitness goals, practicing self-care, and nurturing your overall well-being can positively impact self-esteem.", ]
    ],
    [
        r"How can I practice self-compassion in my wellness journey?",
        ["Be kind to yourself, celebrate progress, and understand that setbacks are a natural part of the wellness journey. Practice self-compassion.", ]
    ],
    [
        r"What's the role of gratitude in overall wellness?",
        ["Cultivating gratitude can improve mental well-being. Consider incorporating gratitude exercises, like journaling, into your wellness routine.", ]
    ],
    [
        r"How can I improve my posture as part of my wellness goals?",
        ["Incorporate exercises that strengthen core muscles, and be mindful of your posture throughout the day. Regular breaks for stretching can help too.", ]
    ],
    [
        r"Can wellness routines help with better time management?",
        ["Yes, prioritizing wellness can enhance your overall productivity and time management skills by promoting physical and mental well-being.", ]
    ],
    [
        r"What's the impact of environmental wellness on my overall health?",
        ["Consider factors like clean air, outdoor activities, and sustainable practices. A healthy environment positively influences overall wellness.", ]
    ],
    [
        r"How can I find motivation to stick to my wellness routine?",
        ["Set realistic goals, find activities you enjoy, and surround yourself with supportive individuals. Motivation often stems from a positive mindset.", ]
    ],
    [
        r"How do I know if I'm pushing myself too hard in my wellness routine?",
        ["Pay attention to signs of overtraining, such as persistent fatigue, soreness, or changes in mood. Balance is key to a sustainable wellness routine.", ]
    ],
    [
        r"Can wellness routines help with building resilience?",
        ["Yes, a holistic wellness routine that includes physical, mental, and emotional well-being can contribute to building resilience in the face of challenges.", ]
    ],
    [
        r"How can I maintain a sense of joy and playfulness in my wellness journey?",
        ["Incorporate activities you love, experiment with different workouts, and don't forget to have fun. Joy is an essential part of overall wellness.", ]
    ],
    [
        r"(thankyou|thankyou so much)",
        ["No problem, anything else?", ]
    ],
    [
        r"can you generate an image?",
        ["Unfortunately no.", ]
    ],
    [
        r"how old are you?",
        ["You don't need to know that!!!", ]
    ],
    [
        r"tell me a joke",
        ["What did one ocean say to the other ocean? Nothing, they just waved.", ]
    ],
    [
        r"Who is the most beautiful person in the world?",
        ["None other than, Dr. Tess Tolentino", ]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day.", ]
    ],
]
