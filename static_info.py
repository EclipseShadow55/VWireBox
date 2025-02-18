from twitchAPI.object.api import CharityCampaign
from twitchAPI.type import AuthScope as AS
from twitchAPI.object.eventsub import ChannelFollowEvent, ChannelSubscribeEvent, ChannelCheerEvent, \
    ChannelSubscriptionEndEvent, ChannelSubscriptionMessageEvent, ChannelRaidEvent, \
    ChannelPointsCustomRewardRedemptionAddEvent, GoalEvent, HypeTrainEvent, CharityCampaignStartEvent, \
    StreamOnlineEvent, StreamOfflineEvent, CharityCampaignProgressEvent, CharityCampaignStopEvent, \
    ChannelChatMessageEvent, ChannelModerateEvent


SUBLIST = {
    "Follow": [[lambda esub, user_id: esub.listen_channel_follow_v2(broadcaster_user_id=user_id, moderator_user_id=user_id, callback=ChannelFollowEvent)],
               [AS.MODERATOR_READ_FOLLOWERS]],
    "Subscribe": [[lambda esub, user_id: esub.listen_channel_subscribe(broadcaster_user_id=user_id, callback=ChannelSubscribeEvent),
                   lambda esub, user_id: esub.listen_channel_subscription_gift(broadcaster_user_id=user_id, callback=ChannelSubscriptionEndEvent),
                   lambda esub, user_id: esub.listen_channel_subscription_message(broadcaster_user_id=user_id, callback=ChannelSubscriptionMessageEvent)],
                  [AS.CHANNEL_READ_SUBSCRIPTIONS]],
    "Cheer": [[lambda esub, user_id: esub.listen_channel_cheer(broadcaster_user_id=user_id, callback=ChannelCheerEvent)], [AS.BITS_READ]],
    "Raid Out": [[lambda esub, user_id: esub.listen_channel_raid(from_broadcaster_user_id=user_id, callback=ChannelRaidEvent)], [AS.CHANNEL_READ_SUBSCRIPTIONS]],
    "Raid In": [[lambda esub, user_id: esub.listen_channel_raid(to_broadcaster_user_id=user_id, callback=ChannelRaidEvent)], [AS.CHANNEL_READ_SUBSCRIPTIONS]],
    "Redeem": [[lambda esub, user_id: esub.listen_channel_points_custom_reward_redemption_add(broadcaster_user_id=user_id, callback=ChannelPointsCustomRewardRedemptionAddEvent)], [AS.CHANNEL_READ_REDEMPTIONS]],
    "Goal Start": [[lambda esub, user_id: esub.listen_goal_begin(broadcaster_user_id=user_id, callback=GoalEvent)], [AS.CHANNEL_READ_GOALS]],
    "Goal Progress": [[lambda esub, user_id: esub.listen_goal_progress(broadcaster_user_id=user_id, callback=GoalEvent)], [AS.CHANNEL_READ_GOALS]],
    "Goal End": [[lambda esub, user_id: esub.listen_goal_end(broadcaster_user_id=user_id, callback=GoalEvent)], [AS.CHANNEL_READ_GOALS]],
    "Hype Train Start": [[lambda esub, user_id: esub.listen_hype_train_begin(broadcaster_user_id=user_id, callback=HypeTrainEvent)], [AS.CHANNEL_READ_HYPE_TRAIN]],
    "Hype Train Progress": [[lambda esub, user_id: esub.listen_hype_train_progress(broadcaster_user_id=user_id, callback=HypeTrainEvent)], [AS.CHANNEL_READ_HYPE_TRAIN]],
    "Hype Train End": [[lambda esub, user_id: esub.listen_hype_train_end(broadcaster_user_id=user_id, callback=HypeTrainEvent)], [AS.CHANNEL_READ_HYPE_TRAIN]],
    "Start Stream": [[lambda esub, user_id: esub.listen_stream_online(broadcaster_user_id=user_id, callback=StreamOnlineEvent)], []],
    "End Stream": [[lambda esub, user_id: esub.listen_stream_offline(broadcaster_user_id=user_id, callback=StreamOfflineEvent)], []],
    "Charity Start": [[lambda esub, user_id: esub.listen_charity_campaign_start(broadcaster_user_id=user_id, callback=CharityCampaignStartEvent)], [AS.CHANNEL_READ_CHARITY]],
    "Charity Progress": [[lambda esub, user_id: esub.listen_charity_campaign_progress(broadcaster_user_id=user_id, callback=CharityCampaignProgressEvent)], [AS.CHANNEL_READ_CHARITY]],
    "Charity End": [[lambda esub, user_id: esub.listen_charity_campaign_end(broadcaster_user_id=user_id, callback=CharityCampaignStopEvent)], [AS.CHANNEL_READ_CHARITY]],
    "Charity Donation": [[lambda esub, user_id: esub.listen_charity_campaign_donate(broadcaster_user_id=user_id, callback=CharityCampaign)], [AS.CHANNEL_READ_CHARITY]],
    "Chat Message": [[lambda esub, user_id: esub.listen_channel_chat_message(broadcaster_user_id=user_id, user_id=user_id, callback=ChannelChatMessageEvent)], [AS.USER_READ_CHAT]],
    "Moderator Action": [[lambda esub, user_id: esub.listen_channel_moderate(broadcaster_user_id=user_id, user_id=user_id, callback=ChannelModerateEvent)], [AS.MODERATOR_READ_BLOCKED_TERMS,
                                                                                                                                                             AS.MODERATOR_READ_CHAT_SETTINGS,
                                                                                                                                                             AS.MODERATOR_READ_UNBAN_REQUESTS,
                                                                                                                                                             AS.MODERATOR_READ_BANNED_USERS,
                                                                                                                                                             AS.MODERATOR_READ_CHAT_MESSAGES,
                                                                                                                                                             AS.MODERATOR_READ_WARNINGS,
                                                                                                                                                             AS.MODERATOR_READ_MODERATORS,
                                                                                                                                                             AS.MODERATOR_READ_VIPS]]
}